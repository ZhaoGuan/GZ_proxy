# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from DataBaseFunction.Real_time_data_statistics_SQL import insert_realtime_data
from basefunction.url_analytic import url_analytic


class FilterFunction(object):
    def __init__(self, http_data):
        # http_data = http_data
        self.url = http_data['url']
        self.request_method = http_data['request_method']
        # 协议
        self.request_scheme = http_data['request_scheme']
        self.request_host = http_data['request_host']
        self.request_port = http_data['request_port']
        self.request_path = http_data['request_path']
        self.request_http_version = http_data['request_http_version']
        self.request_headers = http_data['request_headers']
        self.request_content = http_data['request_content']
        self.request_text = http_data['request_text']
        self.response_http_version = http_data['response_http_version']
        self.response_status_code = http_data['response_status_code']
        self.response_reason = http_data['response_reason']
        self.response_headers = http_data['response_headers']
        self.response_content = http_data['response_content']
        self.response_text = http_data['response_text']

    def filter_url(self, filter_url_list):
        url_data = url_analytic(self.url)
        if url_data['port'] == None:
            t_url = url_data['scheme'] + '://' + url_data['host'] + url_data['path']
        else:
            t_url = url_data['scheme'] + '://' + url_data['host'] + ':' + url_data['port'] + url_data['path']
        if filter_url_list == [] or filter_url_list == None:
            return True
        elif t_url in filter_url_list:
            return True
        else:
            return False

    def filter_host(self, filter_host_list):
        # print(self.request_host)
        if filter_host_list == [] or filter_host_list == None:
            return True
        elif self.request_host in filter_host_list:
            return True
        else:
            return False

    # host 是前提
    def filter_path(self, filter_host_path_list):
        print(filter_host_path_list)
        result_list = []
        for host_path in filter_host_path_list:
            filter_host = host_path['host']
            filter_path_list = host_path['path']
            if (filter_host == None) or (filter_path_list == [] or filter_path_list == None):
                result = True
            elif (self.request_host == filter_host) and (self.request_path in filter_path_list):
                result = True
            else:
                result = False
            result_list.append(result)
        if False in result_list:
            return False
        else:
            return True


if __name__ == "__main__":
    data = {'url': '1', 'request_method': '1',
            'request_scheme': '1', 'request_host': '1',
            'request_port': '1', 'request_path': '1',
            'request_http_version': '1', 'request_headers': '1',
            'request_content': '1',
            'response_http_version': '1', 'request_text': '1',
            'response_status_code': '1', 'response_reason': '1',
            'response_headers': '1', 'response_content': '1', 'response_text': '1'}
    FF = FilterFunction(data)
    print(FF.filter_path([]))
