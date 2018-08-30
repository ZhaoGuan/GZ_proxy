# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
import os
import signal
from sanic import Sanic
from sanic.response import json as sanic_json, text as sanic_text
from sanic.blueprints import Blueprint
from basefunction.config_function import config_writer, config_reader
from DataBaseFunction.Filter_match import select_id_filter
import shutil
import subprocess
import multiprocessing

PATH = os.path.dirname(os.path.abspath(__file__))
har = Blueprint('har')

har_file = PATH + '/../HarRecorded'
har_config_path = PATH + '/../temp/Har_Filter.yml'


@har.route('/config', methods=['POST'])
async def har_config(request):
    try:
        os.makedirs(har_file)
    except:
        pass
    form = request.form
    print(form)
    try:
        match_id = form['match'][0]
        match = select_id_filter(int(match_id))['match']
        har_dump = har_file + '/' + form['fileName'][0]
        yml_data = {'match': match, 'har_dump': har_dump}
        print(har_config_path)
        config_writer(yml_data, har_config_path)
        code = 'ok'
        message = 'ok'
    except Exception as e:
        print()
        code = 'error'
        message = e
    return sanic_json({'code': code, "message": message})


@har.route('/file_list')
async def file_list(request):
    try:
        os.makedirs(har_file)
    except:
        pass
    try:
        result = []
        filelist = os.listdir(har_file)
        for file in filelist:
            result.append({'file_name': file})
        data = result
        code = 'ok'
        message = 'ok'
    except:
        data = []
        code = 'error'
        message = 'error'
    return sanic_json({'code': code, "message": message, "data": data})


@har.route('/using_match')
async def using_match(request):
    try:
        data = config_reader(har_config_path)
        data['har_dump'] = data['har_dump'].split('/')[-1]
        code = 'ok'
        message = 'ok'
    except:
        data = {}
        code = 'error'
        message = 'error'
    return sanic_json({'code': code, "message": message, "data": [data]})


@har.route('/clear_har_config')
async def clear_har_config(request):
    try:
        data = config_writer(None, har_config_path)
        code = 'ok'
        message = 'ok'
    except Exception as e:
        print(e)
        message = e
        code = 'error'
    return sanic_json({"code": code, 'message': message, 'data': []})

@har.route('/clear_har_files')
async def clear_har_files(request):
    try:
        shutil.rmtree(har_file)
        os.makedirs(har_file)
        code = 'ok'
        message = 'ok'
    except Exception as e:
        print(e)
        message = e
        code = 'error'
    return sanic_json({"code": code, 'message': message, 'data': []})
