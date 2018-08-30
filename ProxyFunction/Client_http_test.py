# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
import os
import sys
from mitmproxy import flowfilter
from DataBaseFunction.Real_time_data_statistics_SQL import insert_realtime_data


class ClientHttpTest:
    def __init__(self, filter_match):
        self.filter_match = filter_match

    def response(self, flow):
        match_result = flowfilter.match(self.filter_match, flow)
        # print(self.filter_match)

