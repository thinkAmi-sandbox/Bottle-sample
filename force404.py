# -*- coding:utf-8 -*-
from bottle import route, run, abort, error

@route("/")
def top():
    abort(404, "go to 404")
    return "Hello world!"

@error(404)
def error404(error):
    return "Not Found!"

run(host="0.0.0.0", port=8080, debug=True, reloader=True)