#!/user/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from requests.auth import AuthBase

BASE_URL = 'https://api.github.com'
AUTH_TOKEN = 'bf1e0787062a0754b528b4285bb3f3bfdb247ac3'

def construct_url(end_point):
    return '/'.join([BASE_URL, end_point])

class GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        # request with headers
        r.headers["Authorization"] = ' '.join(['token', self.token])
        return r

def base_auth():
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print response.text
    print response.request.headers

def oauth_base():
    headers = dict()
    headers['Authorization'] = 'token %s' % AUTH_TOKEN
    response = requests.get(construct_url('user/emails'), headers=headers)
    print response.text
    print response.request.headers

def oauth_advanced():
    auth = GithubAuth(AUTH_TOKEN)
    response = requests.get(construct_url('user/emails'), auth=auth)
    print response.text
    print response.request.headers

if __name__ == '__main__':
    base_auth()
    oauth_base()
    oauth_advanced()
