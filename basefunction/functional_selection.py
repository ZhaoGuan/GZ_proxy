# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from ProxyFunction.Real_Time import RealTimResponse
from basefunction.filter_function import FilterFunction

data = {'url': '1', 'request_method': '1',
               'request_scheme': '1', 'request_host': '1',
               'request_port': '1', 'request_path': '1',
               'request_http_version': '1', 'request_headers': '1',
               'request_content': '1',
               'response_http_version': '1', 'request_text': '1',
               'response_status_code': '1', 'response_reason': '1',
               'response_headers': '1', 'response_content': '1', 'response_text': '1'}
FF = FilterFunction(data)


def select_function(function_name, parameter={}):
    functions = {
        "RealTimResponse": lambda: RealTimResponse(),
        'Filter_url': lambda: FF.filter_url(parameter['filter_url_list']),
        'Filter_host': lambda: FF.filter_host(parameter['filter_host_list']),
        'Filter_path': lambda: FF.filter_path(parameter['filter_host_list'], parameter['filter_path_list']),
    }
    return functions[function_name]()


if __name__ == "__main__":
    a = [select_function('Filter_url', {'filter_url_list': []}),
         select_function('Filter_host', {'filter_host_list': []})]
    print(a)
