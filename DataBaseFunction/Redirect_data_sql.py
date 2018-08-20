# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import os
import sys
import sqlite3
import json

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PATH + '/..')

conn = sqlite3.connect(PATH + '/../ProxyDataBase.db')
cursor = conn.cursor()


def create_redirect():
    cursor.execute(
        'create table Fedirect (id integer PRIMARY KEY autoincrement, ' +
        'type varchar(255),' +
        'function varchar(255), ' +
        'parameter varchar(255),' +
        'describe varchar(255))')
    conn.commit()


def insert_redirect_data(type_name, function_name, parameter, describe=''):
    try:
        create_redirect()
    except:
        pass
    cursor.execute(
        'insert into Fedirect (type,function,parameter,describe) values (?,?,?,?)',
        (type_name, function_name, parameter, describe))
    conn.commit()


def select_redirect_all():
    result = []
    cursor.execute('select * from Fedirect')
    select_result = cursor.fetchall()
    for data in select_result:
        id = data[0]
        type_name = data[1]
        function = data[2]
        parameter = data[3]
        describe = data[4]
        result.append({'id': id, 'type': type_name, 'function': function, 'parameter': json.loads(parameter),
                       'describe': describe})
    return result


def select_id_redirect(select_id):
    try:
        create_redirect()
    except:
        pass
    cursor.execute('select * from Fedirect where id=%d' % select_id)
    select_result = cursor.fetchall()
    for data in select_result:
        id = data[0]
        type_name = data[1]
        function = data[2]
        parameter = data[3]
        describe = data[4]
    result = ({'id': id, 'type': type_name, 'function': function, 'parameter': json.loads(parameter),
               'describe': describe})
    return result


def select_redirect_with_id(select_id):
    result = []
    cursor.execute('select * from Fedirect where id=%s' % select_id)
    select_result = cursor.fetchall()
    print(select_result)
    for data in select_result:
        id = data[0]
        type_name = data[1]
        function = data[2]
        parameter = data[3]
        describe = data[4]
        result = ({'id': id, 'type': type_name, 'function': function, 'parameter': json.loads(parameter),
                   'describe': describe})
    return result


def select_id_delete_redirect(select_id):
    try:
        create_redirect()
    except:
        pass
    cursor.execute('DELETE FROM Fedirect WHERE id = %d' % select_id)
    conn.commit()


def delete_redirect_table():
    cursor.execute('DROP TABLE Fedirect')
    conn.commit()
    create_redirect()


if __name__ == "__main__":
    create_redirect()
    # delete_realtime_table()
    # insert_redirect_data('request', 'RedirectUrl',
    #                      '{"url": "https://api.kikakeyboard.com/v1/sticker2/MagicText/all", "new_url": "http://sticker.pre.kikakeyboard.com/backend-content-sending/v1/sticker2/MagicText/all"}')
    select_redirect_all()
    a = select_redirect_all()
    for i in a:
        print(i)
        print('!!!!!!!!!!!!!!!')
    a = select_redirect_with_id('2')
    print(a)
