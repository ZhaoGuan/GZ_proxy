# -*- coding: utf-8 -*-
"""
将flow中符合har_filter['match']的请求和响应写入har_filter['har_dump']对应的文件中
"""

import json
import base64
import zlib
import os
import typing  # noqa

from datetime import datetime
from datetime import timezone

import mitmproxy

from mitmproxy import connections  # noqa
from mitmproxy import version
from mitmproxy import ctx
from mitmproxy.utils import strutils
from mitmproxy.net.http import cookies
from mitmproxy import flowfilter

HAR: typing.Dict = {}

# A list of server seen till now is maintained so we can avoid
# using 'connect' time for entries that use an existing connection.
SERVERS_SEEN: typing.Set[connections.ServerConnection] = set()


class WriteHar:
    def __init__(self, har_filter):
        try:
            self.filter_match = har_filter['match']
        except:
            self.filter_match = None
        try:
            self.har_dump = har_filter['har_dump']
        except:
            self.har_dump = None

    def configure(self, updated):
        HAR.update({
            "log": {
                "version": "1.2",
                "creator": {
                    "name": "mitmproxy har_dump",
                    "version": "0.1",
                    "comment": "mitmproxy version %s" % version.MITMPROXY
                },
                "entries": []
            }
        })

    def response(self, flow):
        """
           Called when a server response has been received.
        """
        try:
            match_result = flowfilter.match(self.filter_match, flow)
            print(match_result)
            print(self.filter_match)
            if match_result:
                print('!!!!!!!')
                # -1 indicates that these values do not apply to current request
                ssl_time = -1
                connect_time = -1

                if flow.server_conn and flow.server_conn not in SERVERS_SEEN:
                    connect_time = (flow.server_conn.timestamp_tcp_setup -
                                    flow.server_conn.timestamp_start)

                    if flow.server_conn.timestamp_tls_setup is not None:
                        ssl_time = (flow.server_conn.timestamp_tls_setup -
                                    flow.server_conn.timestamp_tcp_setup)

                    SERVERS_SEEN.add(flow.server_conn)

                # Calculate raw timings from timestamps. DNS timings can not be calculated
                # for lack of a way to measure it. The same goes for HAR blocked.
                # mitmproxy will open a server connection as soon as it receives the host
                # and port from the client connection. So, the time spent waiting is actually
                # spent waiting between request.timestamp_end and response.timestamp_start
                # thus it correlates to HAR wait instead.
                # 从时间戳计算原始时间。 由于缺乏衡量它的方法，无法计算DNS计时。
                #  HAR被阻止也是如此。 mitmproxy将在从客户端连接接收主机和端口后立即打开服务器连接。
                #  因此，等待的时间实际上是在request.timestamp_end和response.timestamp_start之间等待，因此它与HAR等待相关。
                timings_raw = {
                    'send': flow.request.timestamp_end - flow.request.timestamp_start,
                    'receive': flow.response.timestamp_end - flow.response.timestamp_start,
                    'wait': flow.response.timestamp_start - flow.request.timestamp_end,
                    'connect': connect_time,
                    'ssl': ssl_time,
                }

                # HAR timings are integers in ms, so we re-encode the raw timings to that format.
                timings = dict([(k, int(1000 * v)) for k, v in timings_raw.items()])

                # full_time is the sum of all timings.
                # Timings set to -1 will be ignored as per spec.
                full_time = sum(v for v in timings.values() if v > -1)

                started_date_time = datetime.fromtimestamp(flow.request.timestamp_start, timezone.utc).isoformat()

                # Response body size and encoding
                response_body_size = len(flow.response.raw_content)
                response_body_decoded_size = len(flow.response.content)
                response_body_compression = response_body_decoded_size - response_body_size

                entry = {
                    "startedDateTime": started_date_time,
                    "time": full_time,
                    "request": {
                        "method": flow.request.method,
                        "url": flow.request.url,
                        "httpVersion": flow.request.http_version,
                        "cookies": self.format_request_cookies(flow.request.cookies.fields),
                        "headers": self.name_value(flow.request.headers),
                        "queryString": self.name_value(flow.request.query or {}),
                        "headersSize": len(str(flow.request.headers)),
                        "bodySize": len(flow.request.content),
                    },
                    "response": {
                        "status": flow.response.status_code,
                        "statusText": flow.response.reason,
                        "httpVersion": flow.response.http_version,
                        "cookies": self.format_response_cookies(flow.response.cookies.fields),
                        "headers": self.name_value(flow.response.headers),
                        "content": {
                            "size": response_body_size,
                            "compression": response_body_compression,
                            "mimeType": flow.response.headers.get('Content-Type', '')
                        },
                        "redirectURL": flow.response.headers.get('Location', ''),
                        "headersSize": len(str(flow.response.headers)),
                        "bodySize": response_body_size,
                    },
                    "cache": {},
                    "timings": timings,
                }

                # Store binary data as base64
                if strutils.is_mostly_bin(flow.response.content):
                    entry["response"]["content"]["text"] = base64.b64encode(flow.response.content).decode()
                    entry["response"]["content"]["encoding"] = "base64"
                else:
                    entry["response"]["content"]["text"] = flow.response.get_text(strict=False)

                if flow.request.method in ["POST", "PUT", "PATCH"]:
                    params = [
                        {"name": a, "value": b}
                        for a, b in flow.request.urlencoded_form.items(multi=True)
                    ]
                    entry["request"]["postData"] = {
                        "mimeType": flow.request.headers.get("Content-Type", ""),
                        "text": flow.request.get_text(strict=False),
                        "params": params
                    }

                if flow.server_conn.connected():
                    entry["serverIPAddress"] = str(flow.server_conn.ip_address[0])

                HAR["log"]["entries"].append(entry)
                self.done_write()
            else:
                pass
        except:
            pass

    def done_write(self):
        """
            Called once on script shutdown, after any other events.
        """
        if self.har_dump:
            with open(self.har_dump, "w") as f:
                json_dump: str = json.dumps(HAR, indent=2)
                f.write(json_dump)

    def format_cookies(self, cookie_list):
        rv = []

        for name, value, attrs in cookie_list:
            cookie_har = {
                "name": name,
                "value": value,
            }

            # HAR only needs some attributes
            for key in ["path", "domain", "comment"]:
                if key in attrs:
                    cookie_har[key] = attrs[key]

            # These keys need to be boolean!
            for key in ["httpOnly", "secure"]:
                cookie_har[key] = bool(key in attrs)

            # Expiration time needs to be formatted
            expire_ts = cookies.get_expiration_ts(attrs)
            if expire_ts is not None:
                cookie_har["expires"] = datetime.fromtimestamp(expire_ts, timezone.utc).isoformat()

            rv.append(cookie_har)

        return rv

    def format_request_cookies(self, fields):
        return self.format_cookies(cookies.group_cookies(fields))

    def format_response_cookies(self, fields):
        return self.format_cookies((c[0], c[1][0], c[1][1]) for c in fields)

    def name_value(self, obj):
        """
            Convert (key, value) pairs to HAR format.
        """
        return [{"name": k, "value": v} for k, v in obj.items()]
