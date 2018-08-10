# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from mitmproxy.net.http import cookies


def response(flow):
    if 'picinfo/upload?' in flow.request.url:
        print('!!!!!!!!!!!!!!!!!')
        print(flow.request.url)
        print(flow.response.status_code)
        flow.response.status_code = 504
        print(flow.response.status_code)
