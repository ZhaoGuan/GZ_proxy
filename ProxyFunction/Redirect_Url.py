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
        try:
            self.redirect_request_list = redirect_list['Request']
        except:
            self.redirect_request_list = []
        try:
            self.redirect_response_list = redirect_list['Response']
        except:
            self.redirect_response_list = []
        # print(self.redirect_request_list)
        # print(self.redirect_response_list)

    def request(self, flow):
        if self.redirect_request_list == None:
            pass
        elif isinstance(self.redirect_request_list, list):
            for redirect in self.redirect_request_list:
                select_redirect_function(flow, redirect['Function'], redirect['Parameter'])
        else:
            select_redirect_function(flow, self.redirect_request_list['Function'],
                                     self.redirect_request_list['Parameter'])

    def response(self, flow):
        # print(flow.response.text)
        if self.redirect_response_list == None:
            pass
        elif isinstance(self.redirect_response_list, list):
            for redirect in self.redirect_response_list:
                select_redirect_function(flow, redirect['Function'], redirect['Parameter'])
        else:
            select_redirect_function(flow, self.redirect_response_list['Function'],
                                     self.redirect_response_list['Parameter'])
        # print(flow.response.text)
