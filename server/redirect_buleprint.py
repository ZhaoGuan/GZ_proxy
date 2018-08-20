# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
from sanic import Sanic
from sanic.response import json as sanic_json, text as sanic_text
from sanic.blueprints import Blueprint
from DataBaseFunction.Redirect_data_sql import select_redirect_all, insert_redirect_data, delete_redirect_table, \
    select_id_delete_redirect, select_id_redirect
from basefunction.config_function import rewriter_config, clear_config_key, config_reader

selected_Redirect_path = './temp/Redirect.yml'
redirect = Blueprint('redirect')


@redirect.route('/AllRedirect')
async def show_all_redirect(request):
    db_data = select_redirect_all()
    for i in db_data:
        temp = ''
        for key, value in i['parameter'].items():
            temp = temp + key + ' : ' + value + '\n'
        i['parameter'] = temp
    return sanic_json({"data": db_data})


# request
@redirect.route('/RequestRedirect')
async def show_all_RequestRedirect(request):
    db_data = select_redirect_all()
    request_list = []
    for data in db_data:
        if data['type'] == 'request':
            temp = ''
            for key, value in data['parameter'].items():
                temp = temp + key + ' : ' + value + '\n'
            data['parameter'] = temp
            request_list.append(data)
    return sanic_json({"Request": request_list})


@redirect.route('/add_RequestRedirectUrl', methods=['POST'])
async def add_RequestRedirectUrl(request):
    print(request.form)
    function_name = request.form['function_name'][0]
    url = request.form['Url'][0]
    newurl = request.form['newUrl'][0]
    parameter = json.dumps({"url": url, 'new_url': newurl})
    try:
        describe = request.form['describe'][0]
    except:
        describe = ''
    try:
        insert_redirect_data('Request', function_name, parameter, describe)
        code = 'ok'
        message = ''
    except Exception as e:
        print(e)
        message = e
        code = 'error'
    return sanic_json({"code": code, 'message': message})


@redirect.route('/add_RequestRedirectHost', methods=['POST'])
async def add_RequestRedirectHost(request):
    print(request.form)
    function_name = request.form['function_name'][0]
    host = request.form['Host'][0]
    newhost = request.form['newHost'][0]
    parameter = json.dumps({"host": host, 'new_host': newhost})
    try:
        describe = request.form['describe'][0]
    except:
        describe = ''
    try:
        insert_redirect_data('Request', function_name, parameter, describe)
        code = 'ok'
        message = ''
    except Exception as e:
        print(e)
        message = e
        code = 'error'
    return sanic_json({"code": code, 'message': message})


@redirect.route('/clear_RequestRedirect')
async def clear_RequestRedirect(request):
    try:
        delete_redirect_table()
        code = 'ok'
    except:
        code = 'error'
    return sanic_json({'code': code})


@redirect.route('/delete_RequestRedirect', methods=['POST'])
async def delete_RequestRedirect(request):
    print(request.form)
    select_id = int(request.form['id'][0])
    try:
        select_id_delete_redirect(select_id)
        code = 'ok'
        message = ''
    except Exception as e:
        print(e)
        message = e
        code = 'error'
    return sanic_json({"code": code, 'message': message})


@redirect.route('/select_RequestRedirect', methods=['POST'])
async def select_RequestRedirect(request):
    print(request.form)
    select_id = int(request.form['id'][0])
    try:
        db_data = select_id_redirect(select_id)
        print(db_data)
        data = {'Function': db_data['function'], 'Parameter': db_data['parameter']}
        data_type = db_data['type']
        rewriter_config(data_type, data, selected_Redirect_path)
        code = 'ok'
        message = ''
    except Exception as e:
        print(e)
        message = e
        code = 'error'
    return sanic_json({"code": code, 'message': str(message)})


@redirect.route('/clear_selected_RequestRedirect')
async def clear_selected_RequestRedirect(request):
    try:
        clear_config_key("Request", [], selected_Redirect_path)
        clear_config_key("Response", [], selected_Redirect_path)
        code = 'ok'
    except:
        code = 'error'
    return sanic_json({'code': code})


@redirect.route('/using_RequestRedirect')
async def using_RequestRedirect(request):
    try:
        redirect = config_reader(selected_Redirect_path)
        request_data = redirect['Request']
        show_data = []
        if request_data == []:
            show_data = []
        else:
            for i in request_data:
                temp = ''
                for key, value in i['Parameter'].items():
                    temp = temp + key + ' : ' + value + '\n'
                show_data.append({'Function': i['Function'], 'Parameter': temp})
        code = 'ok'
    except Exception as e:
        print(e)
        show_data = ''
        code = 'error'
    return sanic_json({'code': code, 'data': show_data})


# Response

@redirect.route('/ResponseRedirect')
async def show_all_redirect(request):
    db_data = select_redirect_all()
    response_list = []
    for data in db_data:
        if data['type'] == 'request':
            temp = ''
            for key, value in data['parameter'].items():
                temp = temp + key + ' : ' + value + '\n'
            data['parameter'] = temp
            response_list.append(data)
    return sanic_json({"Response": response_list})


@redirect.route('/add_ResponseRedirect', methods=['POST'])
async def add_RedirectResponse(request):
    print(request.form)
    function_name = request.form['function_name'][0]
    url = request.form['Url'][0]
    response = request.form['Response'][0]
    parameter = json.dumps({"url": url, 'response_local_data': response})
    try:
        describe = request.form['describe'][0]
    except:
        describe = ''
    try:
        insert_redirect_data('Response', function_name, parameter, describe)
        code = 'ok'
        message = ''
    except Exception as e:
        print(e)
        message = str(e)
        code = 'error'
    return sanic_json({"code": code, 'message': message})


@redirect.route('/add_ResponseStatusCodeRedirect', methods=['POST'])
async def add_ResponseStatusCodeRedirect(request):
    print(request.form)
    function_name = request.form['function_name'][0]
    url = request.form['Url'][0]
    new_status_code = request.form['NewStatusCode'][0]
    parameter = json.dumps({"url": url, 'new_status_code': new_status_code})
    try:
        describe = request.form['describe'][0]
    except:
        describe = ''
    try:
        insert_redirect_data('Response', function_name, parameter, describe)
        code = 'ok'
        message = ''
    except Exception as e:
        print(e)
        message = str(e)
        code = 'error'
    return sanic_json({"code": code, 'message': message})


@redirect.route('/clear_ResponseRedirect')
async def clear_ResponseRedirect(request):
    try:
        delete_redirect_table()
        code = 'ok'
    except:
        code = 'error'
    return sanic_json({'code': code})


@redirect.route('/delete_ResponseRedirect', methods=['POST'])
async def delete_ResponseRedirect(request):
    print(request.form)
    select_id = int(request.form['id'][0])
    try:
        select_id_delete_redirect(select_id)
        code = 'ok'
        message = ''
    except Exception as e:
        print(e)
        message = e
        code = 'error'
    return sanic_json({"code": code, 'message': message})


@redirect.route('/select_ResponseRedirect', methods=['POST'])
async def select_ResponseRedirect(request):
    print(request.form)
    select_id = int(request.form['id'][0])
    try:
        data = select_id_redirect(select_id)
        print(data)
        data = {'Function': data['function'], 'Parameter': data['parameter']}
        rewriter_config("Response", data, selected_Redirect_path)
        code = 'ok'
        message = ''
    except Exception as e:
        print(e)
        message = e
        code = 'error'
    return sanic_json({"code": code, 'message': str(message)})


@redirect.route('/clear_selected_ResponseRedirect')
async def clear_selected_ResponseRedirect(request):
    try:
        clear_config_key("Response", [], selected_Redirect_path)
        code = 'ok'
    except:
        code = 'error'
    return sanic_json({'code': code})


@redirect.route('/using_ResponseRedirect')
async def using_ResponseRedirect(request):
    try:
        redirect = config_reader(selected_Redirect_path)
        request_data = redirect['Response']
        show_data = []
        if request_data == []:
            show_data = []
        else:
            for i in request_data:
                temp = ''
                for key, value in i['Parameter'].items():
                    temp = temp + key + ' : ' + value + '\n'
                show_data.append({'Function': i['Function'], 'Parameter': temp})
        code = 'ok'
    except Exception as e:
        print(e)
        show_data = ''
        code = 'error'
    return sanic_json({'code': code, 'data': show_data})
