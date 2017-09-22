#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from requests import exceptions
from requests.auth import AuthBase
import xml.dom.minidom
from xml.dom.minidom import parseString as XMLParse
import lxml.etree
from distutils.version import StrictVersion
from fabric.api import *
import logging

SMASH_ADDON = 'http://mediarepos.net/Repos/smashrepo/addons.xml'
EXODUS_ID = 'plugin.video.exodus'
API_RELEASE_URL = 'https://api.github.com/repos/huberyhe/plugin.video.exodus/releases'
API_TAG_URL = 'https://api.github.com/repos/huberyhe/plugin.video.exodus/tags'
REPO_DIR = '~www/git_repo/plugin.video.exodus'
USER_AGENT = 'Kodi/15.2 (X11; Linux x86_64) Ubuntu/14.04 App_Bitness/64 Version/15.2-Git:02e7013'
CONSOLE_OUTPUT = False

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/home/www/tmp/log/update_exodus_repo.log',
                filemode='a')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)-8s %(message)s')
console.setFormatter(formatter)
if CONSOLE_OUTPUT: logging.getLogger('').addHandler(console)
#################################################################################################

def download_xml(url):
	headers = dict()
	headers['User-Agent'] = USER_AGENT
	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
	except exceptions.Timeout as e:
		logging.warning(e.message)
		return None
	except exceptions.HTTPError as e:
		logging.warning(e.message)
		return None
	except exceptions.ConnectionError as e:
		logging.warning(e.message)
		return None
	else:
		return response.content
	finally:
		pass

def correct_xml(xml_text):
	return xml_text.replace('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', '')

def parse_lxml(xml_text):
	try:
		DOMTree = lxml.etree.fromstring(xml_text)
	except Exception, e:
		logging.warning(e.message)
		return None
	else:
		pass
	finally:
		pass

def parse_xml(xml_text):
	try:
		DOMTree = XMLParse(xml_text)
	except Exception, e:
		logging.warning(e.message)
		return None
	else:
		pass
	finally:
		pass

	addon_info = dict()
	collection = DOMTree.documentElement
	addons = collection.getElementsByTagName('addon')
	require_idx = 0
	for addon in addons:
		if addon.getAttribute('id') == EXODUS_ID:
			addon_info['name'] = addon.getAttribute('name')
			addon_info['id'] = addon.getAttribute('id')
			addon_info['version'] = addon.getAttribute('version')
			news = addon.getElementsByTagName('news')[0]
			addon_info['news'] = news.childNodes[0].data
			requires = addon.getElementsByTagName('requires')[0]
			requires_imports = requires.getElementsByTagName('import')
			addon_info['requires'] = list()
			for requires_import in requires_imports:
				addon_info['requires'].append(dict((['addon', requires_import.getAttribute('addon')], ['version', requires_import.getAttribute('version')])))
			break
	return addon_info

def construct_url(end_point):
	return '/'.join([API_RELEASE_URL, end_point])

class GithubAuth(AuthBase):
	def __init__(self, token_file):
		with open(token_file, 'r') as f:
			self.token = f.read()

	def __call__(self, r):
		# request with headers
		r.headers["Authorization"] = ' '.join(['token', self.token])
		return r

def last_release():
	url = construct_url('latest')
	try:
		response = requests.get(url, auth=auth)
		response.raise_for_status()
	except exceptions.Timeout as e:
		print e.message
		return None
	except exceptions.HTTPError as e:
		print e.message
		return None
	else:
		return response.json()
	finally:
		pass

def delete_release(id):
	url = construct_url(str(id))
	response = requests.delete(url, auth=auth)
	logging.info(response.text)

def create_release(version, commet):
	data = dict()
	data['tag_name'] = version
	data['body'] = commet
	data['name'] = version
	response = requests.post(API_RELEASE_URL, json=data, auth=auth)
	logging.info(response.text)

def update_git(zip_url, version, commet):
	with lcd(REPO_DIR):
		local('wget -q %s -O plugin.video.exodus.zip' % zip_url)
		local('unzip -q plugin.video.exodus.zip')
		local('cp plugin.video.exodus/* ./ -Ra')
		local('rm plugin.video.exodus* -rf')
		local('git commit -a -m "%s"' % commet)
		# local('git tag -a %s -m %s' % (version, commet))
		local('git push origin master')

if __name__ == '__main__':
	global auth
	auth = GithubAuth('/home/www/.ssh/github_token.txt')
	xml_text = download_xml(SMASH_ADDON)
	if not xml_text: exit()
	xml_text = correct_xml(xml_text)
	exodus_info = parse_xml(xml_text)
	if exodus_info == dict():
		logging.info('No such item in addon.xml.')
		exit()

	zip_url = "http://mediarepos.net/Repos/smashrepo/plugin.video.exodus/%s-%s.zip" % (exodus_info['id'], exodus_info['version'])
	last_rls = last_release()
	if not last_rls or StrictVersion(exodus_info['version']) > StrictVersion(last_rls['name']):
		logging.info('Updating from %s to %s...' % (last_rls['name'], exodus_info['version']))
		print 'Updating from %s to %s...' % (last_rls['name'], exodus_info['version'])
		update_git(zip_url, exodus_info['version'], exodus_info['news'])
		create_release(exodus_info['version'], exodus_info['news'])
		# delete_release(last_rls['id'])
		logging.info('Done!')
	else:
		logging.info('There are no updates currently available.')
