#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_sample_urllib2():
    response = urllib2.urlopen(URL_IP)
    print ">>>>Header: "
    print response.info()
    print ">>>>Body: "
    print "".join([line for line in response.readlines()])

def use_params_urllib2():
    params = urllib.urlencode({'param1': 'value1', 'param2': 'value2'})
    print ">>>>Params: "
    print params
    response = urllib2.urlopen('?'.join([URL_GET, '%s']) %params)
    print ">>>>Code: "
    print response.getcode()
    print ">>>>Header: "
    print response.info()
    print ">>>>Body: "
    print "".join([line for line in response.readlines()])


if __name__ == "__main__":
    print ">>sample urllib2"
    use_sample_urllib2()
    print ">>params urllib2"
    use_params_urllib2()
