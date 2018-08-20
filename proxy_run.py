# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from ProxyFunction.Real_Time import RealTimResponse
from ProxyFunction.Redirect_Url import RedirectUrl
from basefunction.config_function import config_reader
from basefunction.create_filter_match import created_new_match

redirect_list = config_reader('./temp/Redirect.yml')
# 那么问题来了这个filter match 的语法。。。。
# filter_match_data = config_reader('./temp/Filter.yml')
filter_match_data = created_new_match()
print(redirect_list)
print(filter_match_data)
addons = [
    RedirectUrl(redirect_list), RealTimResponse(filter_match_data)
    # RedirectUrl(redirect_list),
    # RealTimResponse(filter_list)
]
