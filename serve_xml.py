# -*- coding:utf-8 -*-
import os
from bottle import route, run, static_file, response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

@route("/xml")
def xml_response():
    response.content_type = 'xml/application'
    xml = '<?xml version="1.0" encoding="UTF-8"?><foo>Hello xml!</foo>'
    return xml

@route("/root")
def xml_at_root():
    # ルート直下にxmlがある場合
    return static_file("root_dir.xml", root="")
    
@route("/static")
def xml_at_static_dir():
    # staticフォルダの下にxmlがある場合
    return static_file("static_dir.xml", root=os.path.join(STATIC_DIR, "xml"))

@route("/download-original")
def download_xml():
    # 元ファイルの名前で、強制的にファイルをダウンロード
    return static_file("static_dir.xml", root=os.path.join(STATIC_DIR, "xml"), download=True)

@route("/download-rename")
def xml_dialog():
    # downloadに指定したファイル名で、強制的にファイルをダウンロード
    return static_file("static_dir.xml", root=os.path.join(STATIC_DIR, "xml"), download="rename.xml")


run(host="0.0.0.0", port=8080, debug=True, reloader=True)