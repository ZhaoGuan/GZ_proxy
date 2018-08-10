# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
from sanic import Sanic
from sanic.response import json as sanic_json, text as sanic_text
from sanic.blueprints import Blueprint
from DataBaseFunction.Real_time_data_statistics_SQL import select_realtime_all

realtime = Blueprint('request')


@realtime.route('/show_all_request')
def show_all_redirect(request):
    db_data = select_realtime_all()
    return sanic_json({'data': db_data})

    # @redirect.route('/select_redirect', methods=["POST", ])
    # def select_redirect(request):
    #     body = request.body.decode()
    #     print(body)
    #     return sanic_json(json.loads(body))
