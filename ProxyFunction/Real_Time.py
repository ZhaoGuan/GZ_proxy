# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
import os
import sys

from DataBaseFunction.Real_time_data_statistics_SQL import insert_realtime_data
from basefunction.filter_function import FilterFunction


# from ProxyFunction.url import WritUrl


class RealTimResponse:
    def __init__(self, filte_list):
        # self.url = ''
        # self.request_method = ''
        # 协议
        # self.request_scheme = ''
        # self.request_host = ''
        # self.request_port = ''
        # self.request_path = ''
        # self.request_http_version = ''
        # self.request_headers = ''
        # self.request_content = ''
        # self.request_text = ''
        # self.response_http_version = ''
        # self.response_status_code = ''
        # self.response_reason = ''
        # self.response_headers = ''
        # self.response_content = ''
        # self.response_text = ''
        # 在过滤功能和重定向功能同时开始的时候记得要将重定向放入过滤列表
        self.filter_url_list = filte_list['FilterUrl']
        self.filter_host_list = filte_list['FilterHost']
        self.filter_path_list = filte_list['FilterPath']

    def request(self, flow):
        self.url = str(flow.request.url)
        self.request_method = flow.request.method
        # 协议
        self.request_scheme = flow.request.scheme
        self.request_host = flow.request.host
        self.request_port = flow.request.port
        self.request_path = flow.request.path
        self.request_http_version = flow.request.http_version
        temp_header = {}
        for key, value in flow.request.headers.items():
            temp_header.update({key: value})
        self.request_headers = json.dumps(temp_header)
        self.request_content = flow.request.content
        self.request_text = flow.request.text

    def response(self, flow):
        self.response_http_version = flow.response.http_version
        self.response_status_code = flow.response.status_code
        self.response_reason = flow.response.reason
        temp_header = {}
        for key, value in flow.request.headers.items():
            temp_header.update({key: value})
        self.response_headers = json.dumps(temp_header)
        self.response_content = flow.response.content
        self.response_text = flow.response.text
        http_data = {'url': self.url, 'request_method': self.request_method,
                     'request_scheme': self.request_scheme, 'request_host': self.request_host,
                     'request_port': self.request_port, 'request_path': self.request_path,
                     'request_http_version': self.request_http_version, 'request_headers': self.request_headers,
                     'request_content': self.request_content, 'request_text': self.request_text,
                     'response_http_version': self.response_http_version,
                     'response_status_code': self.response_status_code, 'response_reason': self.response_reason,
                     'response_headers': self.response_headers, 'response_content': self.response_content,
                     'response_text': self.response_text}
        FF = FilterFunction(http_data)
        FF_list = [FF.filter_url(self.filter_url_list), FF.filter_host(self.filter_host_list),
                   FF.filter_path(self.filter_host_list, self.filter_path_list)]
        if False in FF_list:
            pass
        else:
            # 写入数据库
            insert_realtime_data(self.url, self.request_method, self.request_scheme, self.request_host,
                                 self.request_port,
                                 self.request_path, self.request_http_version, self.request_headers,
                                 self.request_content,
                                 self.response_http_version, self.response_status_code, self.response_reason,
                                 self.response_headers,
                                 self.response_content, self.response_text)
