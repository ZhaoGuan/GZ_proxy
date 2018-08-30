# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
with open('./dump.har') as f:
    a = f.read()
    print(json.loads(a))
