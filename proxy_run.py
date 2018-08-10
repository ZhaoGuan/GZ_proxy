# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from ProxyFunction.Real_Time import RealTimResponse
from ProxyFunction.Redirect_Url import RedirectUrl
from basefunction.config_function import config_reader

redirect_list = config_reader('./temp/Redirect.yml')
# 那么问题来了这个filter match 的语法。。。。
filter_list = config_reader('./temp/Filter.yml')
print(redirect_list)
print(filter_list)
addons = [
    RedirectUrl(redirect_list), RealTimResponse(filter_list)
]
