# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import os
from basefunction.config_function import config_reader

PATH = os.path.dirname(os.path.abspath(__file__))
selected_filter_path = PATH + '/../temp/Filter.yml'
selected_redirect_path = PATH + '/../temp/Redirect.yml'


def selected_filter_match_data():
    selected_filter_match = config_reader(selected_filter_path)
    return selected_filter_match


def selected_redirect_url():
    selected_redirect = config_reader(selected_redirect_path)
    print(selected_redirect)
    url_list = []
    if selected_redirect['Request'] != []:
        for request_redirect in selected_redirect['Request']:
            if request_redirect['Function'] == 'RedirectUrl':
                url_list.append(request_redirect['Parameter']['new_url'])
    if selected_redirect['Response'] != []:
        for reqsonse_redirect in selected_redirect['Response']:
            url_list.append(reqsonse_redirect['Parameter']['url'])
    return url_list


def created_new_match():
    old_match_data = selected_filter_match_data()
    redict = selected_redirect_url()
    new_match = ''
    if old_match_data != None:
        old_match = old_match_data['match']
        if redict != []:
            new_match = old_match + ' | '
            for url in redict:
                new_match = new_match + '~u ' + url + ' | '
        else:
            new_match = old_match
    else:
        new_match = None
    return new_match


if __name__ == "__main__":
    # a = selected_filter_match_data()
    # print(a)
    # b = selected_redirect_url()
    # print(b)
    c = created_new_match()
    print(c)
