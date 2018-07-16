# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PATH + '/..')


class WritUrl:
    def request(self, flow):
        url = flow.request.url
        with open('./urllog.txt') as f:
            f.write(url)
