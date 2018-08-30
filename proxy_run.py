# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from ProxyFunction.Real_Time import RealTimResponse
from ProxyFunction.Redirect_Url import RedirectUrl
from basefunction.config_function import config_reader
from basefunction.create_filter_match import created_new_match
from basefunction.write_har import WriteHar

redirect_list = config_reader('./temp/Redirect.yml')
filter_match_data = created_new_match()
har_filter = config_reader('./temp/Har_Filter.yml')
addons = [
    WriteHar(har_filter)
    # WriteHar(har_filter), RedirectUrl(redirect_list), RealTimResponse(filter_match_data)
]
