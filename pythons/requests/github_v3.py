#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from requests import exceptions

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_method():
    response = requests.get(build_uri('users/imoocdemo'), auth=('imoocdemo', 'imoocdemo123'))
    print better_print(response.text)

def json_request():
    response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'),
            json={'name':'babymooc10086'})
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.url
    print response.status_code

def except_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print response.text
        print response.status_code

def session_request():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET', build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), headers=headers)
    prepped = req.prepare()
    resp = s.send(prepped, timeout=5)
    print resp.status_code
    print resp.request.headers
    print resp.text

if __name__ == '__main__':
    json_request()
    request_method()
    except_request()
    session_request()
