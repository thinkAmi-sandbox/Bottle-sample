#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

from bottle import route, request, run, template

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email import charset
from subprocess import Popen, PIPE

SENDER_ADDRESS = 'sender@example.com'
SENDER_LOGIN_ID = 'sender@example.com'
SENDER_PASSWORD = 'passwd'
SENDER_DOMAIN = SENDER_ADDRESS.split('@')[1]
RECIEVER_ADDRESSES = ['receiver1@example.com', 'receiver2@example.com']


@route('/', method="GET")
def form():
    return template('mail.html')
	
@route('/', method="POST")
def send():
    keyvalue = {
        'key': request.forms.get('key_field').decode('utf-8'),
        'value': request.forms.get('value_field').decode('utf-8')
    }
    
    email_body =  """
キー： {key}
値： {value}
""".strip().decode('utf-8').format(**keyvalue)
    
    try:
        msg = MIMEText(email_body, 'plain', 'utf-8')
        msg['Subject'] = Header(u'メールテスト', 'utf-8')
        msg['From'] = SENDER_ADDRESS
        msg['To'] = ','.join(RECIEVER_ADDRESSES)
        
        charset.add_charset('utf-8', charset.SHORTEST, None, 'utf-8')
        
        
        # Sendmail version
        p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
        p.communicate(msg.as_string())
        
        # SMTP Auth(login) version
        smtp_auth_client = smtplib.SMTP(SENDER_DOMAIN, 587)
        smtp_auth_client.login(SENDER_LOGIN_ID, SENDER_PASSWORD)
        smtp_auth_client.sendmail(SENDER_ADDRESS, RECIEVER_ADDRESSES, msg.as_string())
        smtp_auth_client.quit()
        
        # Error version
        smtp_client = smtplib.SMTP(SENDER_DOMAIN, 587)
        smtp_client.sendmail(SENDER_ADDRESS, RECIEVER_ADDRESSES, msg.as_string())
        smtp_client.quit()
        
    except Exception, err:
        return map(str, err)

    return 'sent!'
    
    
if os.name == 'nt':
    # for local
    run(host='0.0.0.0', port=8080, debug=True)
else:
    # for production
    run(server='cgi')