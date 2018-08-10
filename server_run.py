# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from sanic import Sanic, response
from server.redirect_buleprint import redirect
from server.request_buleprint import realtime
from sanic_cors import CORS, cross_origin

app = Sanic()

if __name__ == "__main__":
    app = Sanic()
    CORS(app)
    app.blueprint(redirect, url_prefix='/redirect')
    app.blueprint(realtime, url_prefix='/realtime')
    app.run(host="0.0.0.0", port=8888)
