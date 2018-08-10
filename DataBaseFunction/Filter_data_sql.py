# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import os
import sys
import sqlite3

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PATH + '/..')

conn = sqlite3.connect(PATH + '/../ProxyDataBase.db')
cursor = conn.cursor()


def create_filter():
    cursor.execute(
        'create table Filter (id integer PRIMARY KEY autoincrement, ' +
        'filterurl varchar(255), ' +
        'filterhost varchar(255),' +
        'filterhostpath varchar(255))')
    conn.commit()


def insert_redirect_data(function_name, parameter, describe=''):
    try:
        create_filter()
    except:
        pass
    cursor.execute(
        'insert into Filter (function,parameter,describe) values (?,?,?)',
        (function_name, parameter, describe))
    conn.commit()


def select_redirect_all():
    result = []
    cursor.execute('select * from Filter')
    select_result = cursor.fetchall()
    for data in select_result:
        id = data[0]
        filterurl = data[1]
        filterhost = data[2]
        filterhostpath = data[3]
        result.append({'id': id, 'filterurl': filterurl, 'filterhost': filterhost, 'filterhostpath': filterhostpath})
    return result


def delete_redirect_table():
    cursor.execute('DROP TABLE Filter')
    select_result = cursor.fetchall()
    print(select_result)


if __name__ == "__main__":
    # delete_realtime_table()
    a = select_redirect_all()
    for i in a:
        print(i)
        print('!!!!!!!!!!!!!!!')
