# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from ProxyFunction.Real_Time import RealTimResponse
from ProxyFunction.Redirect_Url import RedirectUrl
from basefunction.config_function import config_reader

redirect_list = config_reader('./temp/Redirect.yml')
filter_list = config_reader('./temp/Filter.yml')
addons = [
    RedirectUrl(redirect_list), RealTimResponse(filter_list)
]
