# -*- coding: utf-8 -*-
# __author__ = 'Gz'

data = [{'query': {'tag': [], 'type': []}, 'response': {'dataformat': {}}, 'url': None},
        {'query': {'tag': [], 'type': []}, 'response': {'dataformat': {}}, 'url': None}]


def case_data(data):
    result = {}
    for case in data:
        result.update({case['url']: {}})
