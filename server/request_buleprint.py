# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
from sanic import Sanic
from sanic.response import json as sanic_json, text as sanic_text
from sanic.blueprints import Blueprint
from DataBaseFunction.Real_time_data_statistics_SQL import select_realtime_all
from DataBaseFunction.Filter_match import select_filter_all, insert_filter_data, select_id_delete_filter, \
    delete_filter_table, select_id_filter
from basefunction.config_function import config_writer, config_reader

realtime = Blueprint('request')

selected_filter_path = './temp/Filter.yml'


@realtime.route('/show_all_request')
def show_all_redirect(request):
    db_data = select_realtime_all()
    return sanic_json({'data': db_data})

    # @redirect.route('/select_redirect', methods=["POST", ])
    # def select_redirect(request):
    #     body = request.body.decode()
    #     print(body)
    #     return sanic_json(json.loads(body))


@realtime.route('/show_all_filter')
def show_all_filter(request):
    try:
        db_data = select_filter_all()
        code = 'ok'
    except:
        db_data = []
        code = 'error'
    return sanic_json({'data': db_data, 'code': code})


@realtime.route('/add_filter', methods=['POST'])
def add_filter(request):
    match = request.form['match'][0]
    try:
        describe = request.form['describe'][0]
    except Exception as e:
        print(e)
        describe = ''
    insert_filter_data(match, describe)
    return sanic_json({"code": "ok"})


@realtime.route('/select_filter', methods=['POST'])
def select_filter(request):
    delete_id = int(request.form['id'][0])
    try:
        select_filter = select_id_filter(delete_id)
        config_writer(select_filter, selected_filter_path)
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
    return sanic_json({"code": code})


@realtime.route('/using_filter')
def using_filter(request):
    try:
        data = config_reader(selected_filter_path)
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
        data = None
    return sanic_json({"code": code, "data": data})


@realtime.route('/delete_filter', methods=['POST'])
def delete_filter(request):
    delete_id = int(request.form['id'][0])
    try:
        select_id_delete_filter(delete_id)
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
    return sanic_json({"code": code})


@realtime.route('/clear_filter')
def clear_filter(request):
    try:
        delete_filter_table()
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
    return sanic_json({"code": code})


@realtime.route('/cancel_filter')
def cancel_filter(request):
    try:
        data = config_writer(None, selected_filter_path)
        code = 'ok'
    except Exception as e:
        print(e)
        code = 'error'
    return sanic_json({"code": code})
