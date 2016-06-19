# -*- coding:utf-8 -*-
from bottle import hook, request, route, run

# from official recipe
# http://bottlepy.org/docs/dev/recipes.html#ignore-trailing-slashes
@hook("before_request")
def strip_path():
    request.environ["PATH_INFO"] = request.environ["PATH_INFO"].rstrip("/")

@route("/slash")
def slash():
    return "Hello world!"

run(host="0.0.0.0", port=8080, debug=True, reloader=True)