# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
import os
import sys
from basefunction.config_function import config_reader

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PATH + '/..')


def single_redirect_data(function_name, Parameter):
    parameter_json = json.loads(Parameter)
    result = {'Function': function_name, 'Parameter': parameter_json}
    return result


def get_redirect_url_host():
    host_list = []
    url_list = []
    host_path_list = []
    request_data = config_reader(PATH + '/../temp/Redirect.yml')['Request']
    if request_data != None:
        for data in request_data:
            Parameter_key = list(data['Parameter'].keys())
            if 'new_url' in Parameter_key:
                url_list.append(data['Parameter']['new_url'])
            elif ('new_host' in Parameter_key) and ('new_path' not in Parameter_key):
                url_list.append(data['Parameter']['new_host'])
            else:
                host_path_list.append({'host': data['Parameter']['new_host'], 'path': data['Parameter']['new_path']})
        return {'host': host_list, 'url': url_list, 'host_path': host_path_list}
    else:
        return None


if __name__ == "__main__":
    a = get_redirect_url_host()
    print(a)
