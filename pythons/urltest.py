#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2

class RedirectHandler(urllib2.HTTPRedirectHandler):
	def http_error_301(self, req, fp, code, msg, headers):
		print 'code',code
		pass
	def http_error_302(self, req, fp, code, msg, headers):
		print 'code',code
		pass

rUrl = "http://www.sina.com"
opener = urllib2.build_opener(RedirectHandler)
# rest = opener.open(rUrl)
rest2 = urllib2.urlopen(rUrl)
# print rest.info()
print rest2.geturl()
print '█'