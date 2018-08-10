# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import os
import sys
import sqlite3

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PATH + '/..')

conn = sqlite3.connect(PATH + '/../ProxyDataBase.db')
cursor = conn.cursor()


def creat_RealTime():
    cursor.execute(
        'create table RealTime (id integer PRIMARY KEY autoincrement, ' +
        'url varchar(255), ' +
        'request_method varchar(255), ' +
        'request_scheme varchar(255), ' +
        'request_host varchar(255), ' +
        'request_port varchar(255), ' +
        'request_path varchar(255), ' +
        'request_http_version varchar(255), ' +
        'request_headers varchar(255), ' +
        'request_content varchar(255), ' +
        'response_http_version varchar(255), ' +
        'response_status_code varchar(255), ' +
        'response_reason varchar(255), ' +
        'response_headers varchar(255), ' +
        'response_content varchar(255), ' +
        'response_text varchar(255))')
    conn.commit()


def insert_realtime_data(url, request_method, request_scheme, request_host, request_port, request_path,
                         request_http_version, request_headers, request_content, response_http_version,
                         response_status_code, response_reason, response_headers, response_content, response_text):
    try:
        creat_RealTime()
    except:
        pass
    cursor.execute(
        'insert into RealTime (url, request_method, request_scheme, request_host, request_port, request_path,' +
        'request_http_version, request_headers, request_content, response_http_version,' +
        'response_status_code, response_reason, response_headers, response_content, response_text) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        (url, request_method, request_scheme, request_host, request_port, request_path,
         request_http_version, request_headers, request_content, response_http_version,
         response_status_code, response_reason, response_headers, response_content, response_text))
    conn.commit()


def select_realtime_all():
    result = []
    cursor.execute('select * from RealTime')
    select_result = cursor.fetchall()
    for data in select_result:
        id = data[0]
        url = data[1]
        request_method = str(data[2])
        request_scheme = str(data[3])
        request_host = str(data[4])
        request_port = str(data[5])
        request_path = str(data[6])
        request_http_version = str(data[7])
        request_headers = str(data[8])
        request_content = str(data[9])
        response_http_version = str(data[10])
        response_status_code = str(data[11])
        response_reason = str(data[12])
        response_headers = str(data[13])
        response_content = str(data[14])
        response_text = str(data[15])
        result.append({'id': id, 'url': url, 'request_method': request_method, 'request_scheme': request_scheme,
                       'request_host': request_host,
                       'request_port': request_port, 'request_path': request_path,
                       'request_http_version': request_http_version, 'request_headers': request_headers,
                       'request_content': request_content,
                       'response_http_version': response_http_version,
                       'response_status_code': response_status_code, 'response_reason': response_reason,
                       'response_headers': response_headers,
                       'response_content': response_content, 'response_text': response_text})
    return result


def delete_realtime_table():
    cursor.execute('DROP TABLE RealTime')
    select_result = cursor.fetchall()
    # print(select_result)


if __name__ == "__main__":
    # delete_realtime_table()
    # try:
    #     creat_RealTime()
    # except:
    #     pass
    a = select_realtime_all()
    for i in a:
        print(i)
        print('!!!!!!!!!!!!!!!')
