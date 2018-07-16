# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from mitmproxy.addons import wsgiapp
from sanic import Sanic, response
from sanic.response import json as sanic_json, text as sanic_reslonse_text
from sanic_dispatcher import SanicDispatcherMiddlewareController

app = Sanic()
dispatcher = SanicDispatcherMiddlewareController(app)

proxapp = Sanic('proxapp')

dispatcher.register_sanic_application(proxapp, "/proxapp", apply_middleware=True)


@app.route('/')
def hello_world(request):
    return sanic_json({"hello": "world"})


@proxapp.route('/index')
async def index(request):
    # return response.text("Hello World from Child App")
    return sanic_reslonse_text(wsgiapp.WSGIApp(app, "proxapp.local", 80))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
