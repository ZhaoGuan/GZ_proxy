# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json

with open('./HarRecorded/kika.har') as f:
    a = f.read()
    print(json.loads(a))


def key_value(data):
    dict_data = {}
    for d in data:
        dict_data.update({d['name']: d['value']})
    return dict_data


def get_har_data():
    # har_data = open_har()
    har_data = a
    har_data_json = json.loads(har_data)
    request_data = har_data_json['log']['entries']
    result = []
    for request in request_data:
        request_data = request['request']
        response_data = request['response']
        for key, value in request_data:
            if isinstance(value, str):
                pass
            elif isinstance(value, list):
                if value == []:
                    request_data[key] = None
                else:
                    request_data[key] = key_value(value)
            elif isinstance(value, dict):
                if value == {}:
                    request_data[key] = None
                else:
                    if value['encoding'] == 'base64':
                        request_data[key] = base64.b64decode(value['text'])
        for key, value in response_data:
            if isinstance(value, str):
                pass
            elif isinstance(value, list):
                if value == []:
                    response_data[key] = None
                else:
                    response_data[key] = key_value(value)
            elif isinstance(value, dict):
                if value == {}:
                    response_data[key] = None
                else:
                    if value['encoding'] == 'base64':
                        response_data[key] = base64.b64decode(value['text'])
        result.append({'request': request_data, 'response': request_data})
    return result
