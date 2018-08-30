# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import json
import os
import signal
from sanic import Sanic
from sanic.response import json as sanic_json, text as sanic_text
from sanic.blueprints import Blueprint
from DataBaseFunction.Redirect_data_sql import select_redirect_all
import subprocess
import multiprocessing

PATH = os.path.dirname(os.path.abspath(__file__))
run_proxy = Blueprint('run_proxy')

cmd = 'mitmdump -p 8192 -s ' + PATH + '/../proxy_run.py'
multiprocessing.freeze_support()
pool = multiprocessing.Pool(1)

proxy_pid = 0


@run_proxy.route('/')
async def proxy(request):
    global proxy_pid
    global pool
    if proxy_pid != 0:
        os.kill(proxy_pid, signal.SIGKILL)
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proxy_pid = p.pid
    if proxy_pid == 0:
        code = 'error'
        message = '启动失败'
    else:
        code = 'ok'
        message = ''
    return sanic_json({'code': code, "message": message})


@run_proxy.route('/stop')
async def stop_proxy(request):
    global proxy_pid
    if proxy_pid != 0:
        os.kill(proxy_pid, signal.SIGKILL)
    if proxy_pid == 0:
        code = 'error'
        message = '没有启动的Proxy进程'
    else:
        os.kill(proxy_pid, signal.SIGKILL)
        code = 'ok'
        message = '已关闭Proxy进程'
    return sanic_json({'code': code, "message": message})
