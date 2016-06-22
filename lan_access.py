# -*- coding:utf-8 -*-
from bottle import route, run

@route("/")
def access():
    return "OK!"


# hostデフォルト値は、127.0.0.1
# OK - localhost / 127.0.0.1 
# NG - 192.168.0.10 / hostname
# run(port=8080, debug=True, reloader=True)
# run(host="localhost", port=8080, debug=True, reloader=True)

# OK - 192.168.0.10 / hostname
# NG - localhost / 127.0.0.1
run(host="192.168.0.10", port=8080, debug=True, reloader=True)
# run(host="<your hostname>", port=8080, debug=True, reloader=True)

# OK - ALL
# run(host="0.0.0.0", port=8080, debug=True, reloader=True)