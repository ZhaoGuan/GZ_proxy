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


def insert_filter_data(match, describe=''):
    try:
        create_filter()
    except:
        pass
    cursor.execute(
        'insert into FilterMatch (match, describe) values (?,?)', (match, describe))
    conn.commit()


def select_filter_all():
    try:
        create_filter()
    except:
        pass
    result = []
    cursor.execute('select * from FilterMatch')
    select_result = cursor.fetchall()
    for data in select_result:
        id = data[0]
        mathch = data[1]
        describe = data[2]
        result.append({'id': id, 'match': mathch, 'describe': describe})
    return result


def select_id_filter(select_id):
    try:
        create_filter()
    except:
        pass
    result = []
    cursor.execute('select * from FilterMatch where id=%d' % select_id)
    select_result = cursor.fetchall()
    for data in select_result:
        id = data[0]
        mathch = data[1]
        describe = data[2]
    result = {'id': id, 'match': mathch, 'describe': describe}
    return result


def select_id_delete_filter(select_id):
    try:
        create_filter()
    except:
        pass
    cursor.execute('DELETE FROM FilterMatch WHERE id = %d' % select_id)
    conn.commit()


def delete_filter_table():
    cursor.execute('DROP TABLE FilterMatch')
    conn.commit()


if __name__ == "__main__":
    insert_filter_data('~u kika')
    # delete_realtime_table()
    a = select_filter_all()
    for i in a:
        print(i)
        print('!!!!!!!!!!!!!!!')
    # select_id_delete_filter(2)
    print(select_id_filter(2))
    a = select_filter_all()
    print(a)
