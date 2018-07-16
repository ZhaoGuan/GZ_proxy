# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from basefunction.redirect_function import RedirectFunction, select_redirect_function
from basefunction.config_function import config_reader
import yaml

'http://sticker.pre.kikakeyboard.com/backend-content-sending/v1/sticker2/MagicText/all'

"""
"RedirectUrl" :
"RedirectHost":
"RedirectPath":
"RedirectResponseText":
"""
parameter2 = {'url': 'http://sticker.pre.kikakeyboard.com/backend-content-sending/v1/sticker2/MagicText/all',
              'response_local_data': '{"data":{"info":null},"errorMsg":"ok","errorCode":0}'}


class RedirectUrl:
    def __init__(self, redirect_list):
        self.redirect_list = redirect_list

    def request(self, flow):
        for redirect in self.redirect_list:
            select_redirect_function(flow, redirect['Function'], redirect['Parameter'])

    def response(self, flow):
        print(flow.response.text)
        select_redirect_function(flow, 'RedirectResponseText', parameter2)
        print(flow.response.text)
