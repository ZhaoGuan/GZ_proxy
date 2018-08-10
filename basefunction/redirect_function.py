# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from mitmproxy import http
from basefunction.url_analytic import url_analytic, host_analytic


class RedirectFunction:
    def __init__(self, flow):
        self.flow = flow

    def redirect_url(self, url, new_url):
        request_params = url_analytic(self.flow.request.url)['params']
        if url in self.flow.request.url:
            if request_params != None:
                new_url = new_url + '?'
                if isinstance(request_params, dict):
                    for key, value in request_params.items():
                        new_url = new_url + key + '=' + value + '&'
                    self.flow.request.url = new_url[:-1]
                else:
                    self.flow.request.url = new_url + list(request_params.keys())[0] + '=' + \
                                            list(request_params.values())[0]
            else:
                self.flow.request.url = new_url

        else:
            pass


    def redirect_host(self, host, new_host):

        if ':' in new_host:
            new_host = host_analytic(new_host)

        if self.flow.request.host == host:
            if ':' in new_host:
                new_host = host_analytic(new_host)
                self.flow.request.host = new_host['host']
                self.flow.request.port = int(new_host['port'])
            else:
                self.flow.request.host = new_host

    def redirect_path(self, new_host, path, new_path):
        request_params = url_analytic(self.flow.request.url)['params']
        if request_params != None:
            if (self.flow.request.host == new_host) and (self.flow.request.path == path):
                new_path = new_path + '?'
                if isinstance(request_params, dict):
                    for key, value in request_params.items():
                        new_path = new_path + key + '=' + value + '&'
                    self.flow.request.path = new_path[:-1]
                else:
                    self.flow.request.path = new_path + list(request_params.keys())[0] + '=' + \
                                             list(request_params.values())[0]
            self.flow.request.path = new_path
        else:
            pass


    def redirect_response_json(self, url, response_local_data):
        if url in self.flow.request.url:
            self.flow.response.text = response_local_data


def select_redirect_function(flow, function_name, parameter):
    RF = RedirectFunction(flow)
    functions = {
        "RedirectUrl": lambda: RF.redirect_url(parameter['url'], parameter['new_url']),
        "RedirectHost": lambda: RF.redirect_host(parameter['host'], parameter['new_host']),
        "RedirectPath": lambda: RF.redirect_path(parameter['new_host'], parameter['path'], parameter['new_path']),
        "RedirectResponseText": lambda: RF.redirect_response_json(parameter['url'], parameter['response_local_data'])
    }
    return functions[function_name]()
