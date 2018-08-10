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
        'create table FilterMatch (id integer PRIMARY KEY autoincrement, ' +
        'match varchar(255),' +
        'describe varchar(255))')
    conn.commit()


def insert_redirect_data(match, describe=''):
    try:
        create_filter()
    except:
        pass
    cursor.execute(
        'insert into FilterMatch (match, describe) values (?,?)',(match, describe))
    conn.commit()


def select_redirect_all():
    result = []
    cursor.execute('select * from FilterMatch')
    select_result = cursor.fetchall()
    for data in select_result:
        id = data[0]
        mathch = data[1]
        result.append({'id': id, 'FilterMatch': mathch})
    return result


def delete_redirect_table():
    cursor.execute('DROP TABLE FilterMatch')
    select_result = cursor.fetchall()
    print(select_result)


if __name__ == "__main__":
    insert_redirect_data('~u kika')
    # delete_realtime_table()
    a = select_redirect_all()
    for i in a:
        print(i)
        print('!!!!!!!!!!!!!!!')
