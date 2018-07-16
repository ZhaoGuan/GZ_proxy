# -*- coding: utf-8 -*-
# __author__ = 'Gz'

def params_analytic(params):
    params_result = {}
    if isinstance(params, list):
        for params_ in params:
            params__result = params_.split('=')
            params_result.update({params__result[0]: params__result[1]})
    else:
        params__result = params.split('=')
        params_result.update({params__result[0]: params__result[1]})
    return params_result


def host_analytic(host_part):
    host_part = host_part.split(':')
    host = host_part[0]
    port = host_part[1]
    return {'host': host, 'port': port}


def url_analytic(url):
    url_ = url.split('://')
    scheme = url_[0]
    host_port_path = url_[1].split('?')[0].split('/')
    try:
        host_port = host_port_path[0].split(':')
        host = host_port[0]
        port = host_port[1]
    except:
        host = host_port_path[0]
        port = None
    path = '/'
    for path_ in host_port_path[1:]:
        path = path + path_ + '/'
    path = path[:-1]
    try:
        params = url_[1].split('?')[1].split('&')
        params_result = params_analytic(params)
        result = {'scheme': scheme, 'host': host, 'port': port, 'path': path, 'params': params_result}
    except:
        result = {'scheme': scheme, 'host': host, 'port': port, 'path': path, 'params': None}
    return result


if __name__ == "__main__":
    a = url_analytic('https://api.kikakeyboard.com/v1/sticker2/MagicText/all')
    print(a)
