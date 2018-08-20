# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
import os
import sys
from mitmproxy import flowfilter
from DataBaseFunction.Real_time_data_statistics_SQL import insert_realtime_data


class RealTimResponse:
    def __init__(self, filter_match):
        self.filter_match = filter_match['match']
        print(self.filter_match)

    def response(self, flow):
        match_result = flowfilter.match(self.filter_match, flow)
        # print(match_result)
        if match_result:
            insert_realtime_data(flow.request.url, flow.request.method, flow.request.scheme, flow.request.host,
                                 flow.request.port,
                                 flow.request.path, flow.request.http_version, json.dumps(dict(flow.request.headers)),
                                 flow.request.content,
                                 flow.response.http_version, flow.response.status_code, flow.response.reason,
                                 json.dumps(dict(flow.response.headers)),
                                 flow.response.content, flow.response.text)
