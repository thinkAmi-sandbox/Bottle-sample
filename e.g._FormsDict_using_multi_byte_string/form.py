from bottle import Bottle, run, get, post, request, response, jinja2_template


app = Bottle()

@app.get('/')
def get_form():
    cookie_by_get = request.get_cookie('input', '')
    cookie_by_dict_key = request.cookies['input'] if request.get_cookie('input') else ''
    cookie_by_getunicode = request.cookies.getunicode('input', default='')
    cookie_by_attr = request.cookies.input if request.get_cookie('input') else ''
    cookie_by_decode = request.cookies.decode().get('input', '')

    return jinja2_template(
        'form.html',
        cookie_by_get=cookie_by_get,
        cookie_by_dict_key=cookie_by_dict_key,
        cookie_by_getunicode=cookie_by_getunicode,
        cookie_by_attr=cookie_by_attr,
        cookie_by_decode=cookie_by_decode)


@app.post('/')
def post_form():
    response.set_cookie('input', request.forms.get('input'))
    # UnicodeをCookieへセットしようとするとエラーになる
    # 'latin-1' codec can't encode character '\u307e' in position 123: ordinal not in range(256)
    # response.set_cookie('comment', request.forms.getunicode('comment'))

    form_by_get = request.forms.get('input')
    form_by_dict_key = request.forms['input']
    form_by_getunicode = request.forms.getunicode('input')
    form_by_attr = request.forms.input
    form_by_decode = request.forms.decode().get('input')
    form_by_getall = request.forms.getall('input')
    form_by_getall_first = request.forms.getall('input')[0]
    form_by_decode_getall = request.forms.decode().getall('input')
    form_by_decode_getall_first = request.forms.decode().getall('input')[0]

    return jinja2_template(
        'form.html',
        form_by_get=form_by_get,
        form_by_dict_key=form_by_dict_key,
        form_by_getunicode=form_by_getunicode,
        form_by_attr=form_by_attr,
        form_by_decode=form_by_decode,
        form_by_getall=form_by_getall,
        form_by_getall_first=form_by_getall_first,
        form_by_decode_getall=form_by_decode_getall,
        form_by_decode_getall_first=form_by_decode_getall_first)


@app.get('/delete_cookie')
def delete_cookie():
    response.delete_cookie('input')
    redirect('/')


if __name__ == "__main__":
    run(app, host="localhost", port=8080, debug=True, reloader=True)
