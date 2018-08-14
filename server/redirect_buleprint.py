# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
from sanic import Sanic
from sanic.response import json as sanic_json, text as sanic_text
from sanic.blueprints import Blueprint
from DataBaseFunction.Redirect_data_sql import select_redirect_all

redirect = Blueprint('redirect')


@redirect.route('/RequestRedirect')
async def show_all_redirect(request):
    db_data = select_redirect_all()
    request_list = []
    response_list = []
    for data in db_data:
        if data['type'] == 'request':
            request_list.append(data)
        else:
            response_list.append(data)
    return sanic_json({"Request": request_list})


@redirect.route('/ResponseRedirect')
async def show_all_redirect(request):
    db_data = select_redirect_all()
    request_list = []
    response_list = []
    for data in db_data:
        if data['type'] == 'request':
            request_list.append(data)
        else:
            response_list.append(data)
    return sanic_json({"Response": response_list})


@redirect.route('/select_redirect', methods=["POST", ])
async def select_redirect(request):
    body = request.body.decode()
    # print(body)
    return sanic_json(json.loads(body))
