#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_sample_requests():
    response = requests.get(URL_IP)
    print ">>>>Header: "
    print response.headers
    print ">>>>Body: "
    print response.text

def use_params_requests():
    playload = {'param1': 'value1', 'param2': 'value2'}
    response = requests.get(URL_GET, params=playload)
    print ">>>Status: "
    print response.status_code, response.reason
    print ">>>>Header: "
    print response.headers
    print ">>>>Body: "
    print response.json()

if __name__ == '__main__':
    print ">>sample requests"
    use_sample_requests()
    print ">>params requests"
    use_params_requests()
