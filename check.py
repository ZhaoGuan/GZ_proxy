# -*- coding: utf-8 -*-
# __author__ = 'Gz'
url = 'http://34.214.222.244:9090/backend-content-sending/popup?type=0'
url_ = url.split('//')
host_port_path = url_[1].split('?')[0].split('/')
host_port = host_port_path[0].split(':')
host = host_port_path[0].split(':')[0]
port = host_port_path[0].split(':')[1]
path = '/'
for path_ in host_port_path[1:]:
    path = path + path_ + '/'
path = path[:-1]
params = url_[1].split('?')[1].split('&')
params_result = {}
for i in params:
    params__result = i.split('=')
    params_result.update({params__result[0]: params__result[1]})
print(host_port_path)
print(path)
print(host)
print(port)
print(params)
print(list(params_result.keys())[0])
