#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import route, run
import os
import sys
import pkgutil

@route('/all_modules')
def all_modules():
    return ", ".join([module[1] for module in pkgutil.iter_modules()])
    
    # 内包表記なし版
    # result = ""
    # for module in pkgutil.iter_modules():
    #     result += module[1] + ', '
    # return result


@route('/running_modules')
def running_modules():
    formatter = lambda n, m: "{name}:{version}".format(name=n, version=m.__version__)
    modules = [formatter(name, module) for name, module in sorted(sys.modules.items()) if hasattr(module, '__version__')]
    return ", ".join(modules)
    
    # lambda & 内包表記なし版
    # result = ""
    # for name, module in sorted(sys.modules.items()): 
    #     if hasattr(module, '__version__'):
    #         result += "{name}:{version}, ".format(name=name, version=module.__version__)  
    # return result


if os.name == 'nt':
    # for local
    run(host='0.0.0.0', port=8080, debug=True)
else:
    # for production
    run(server='cgi')