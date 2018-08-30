# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from sanic import Sanic, response
from server.redirect_buleprint import redirect
from server.request_buleprint import realtime
from server.run_proxy_buleprint import run_proxy
from server.har_buleprint import har
from sanic_cors import CORS, cross_origin

app = Sanic()

if __name__ == "__main__":
    app = Sanic()
    CORS(app)
    app.blueprint(redirect, url_prefix='/redirect')
    app.blueprint(realtime, url_prefix='/realtime')
    app.blueprint(run_proxy, url_prefix='/run_proxy')
    app.blueprint(har, url_prefix='/har')
    app.static('/dist', './dist')
    app.run(host="0.0.0.0", port=8888, workers=2)
