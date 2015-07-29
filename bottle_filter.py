#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from bottle import route, request, run
from bottle import jinja2_template as template

# 必要に応じて、jinja2テンプレートがあるディレクトリを追加
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append("./path/to/templates")

# jinja2のfilterを設定
from bottle import BaseTemplate
BaseTemplate.settings.update({'filters': {'nl2br': lambda content: content.replace('\n', '<br>')}})


@route('/', method="GET")
def form():
    return template('bottle_filter.html', result="")
	
@route('/', method="POST")
def display():
    input_with_newline = request.forms.get('input_with_newline').decode('utf-8')
    return template('bottle_filter.html', result=input_with_newline)
    

if os.name == 'nt':
    # for local
    run(host='0.0.0.0', port=8080, debug=True)
else:
    # for production
    run(server='cgi')