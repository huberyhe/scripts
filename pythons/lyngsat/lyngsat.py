#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from BeautifulSoup import BeautifulSoup
import sys
import urllib2
import os
import logging

class MyLogging():
	def debug(self, string):
		print string
	def info(self, string):
		print string
	def warnning(self, string):
		print string

class Lyngsat():
	"""docstring for Lyngsat"""

	# 通过degree查找channel所在页面
	def lookup_sat_urls(self, sdg):
		urls_return = []
		links = self.get_sat_links()
		for link in links:
			if link[0] == sdg:
				urls_return.append(link[1])
		return urls_return
	# 在channel页面中查找指定范围freq上指定sid的频道，如果没有找到，进入package页面查找
	def lookup_chn_in_sat(self, url, freq, sid):
		freq = str(freq)
		sid = str(sid)
		logger.info('-> Parsing %s %s %s' % (url,freq,sid))
		chn_name = ''
		chn_freq = ''
		pkg_link = ''
		pkg_links = []
		FOUND = False
		try:
			html_doc = self.get_page_contents(url)
			if html_doc == '':return (False, 'url open failed')
			soup = BeautifulSoup(html_doc)
		except Exception, e:
			ex = sys.exc_info()
			logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
			return (False, 'url parse failed')

		tables = soup.findAll('table', width='720')
		if len(tables) > 1:
			# print 'table num:',len(tables)
			for i in range(0, len(tables)):
				try:
					trs = tables[i].findAll('tr')
				except Exception, e:
					ex = sys.exc_info()
					logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
					break
				for tr in trs:
					tds = tr.findAll('td')
					# first line of a chn_freq
					if len(tds) == 8 and len(tds[0].text) > 2:
						try:
							chn_freqs = tds[0].findAll('b')
						except Exception, e:
							ex = sys.exc_info()
							logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
							break
						chn_freq_content = ''
						if len(chn_freqs) > 0:
							chn_freq_content = chn_freqs[0].text
							# chn_freq_content = '%s%s' % (chn_freq_content.strip().strip('&nbsp;').split('&')[0], chn_freq_content.split(';')[-1])
							chn_freq_content = chn_freq_content.replace(' ','').strip('&nbsp;').split('&')[0]
						# it's what we need
						if chn_freq_content:
							if abs(float(chn_freq_content)- float(freq)) < 6:
								chn_freq = str(chn_freq_content)
								tds2_a = tds[2].findAll('a')
								if len(tds2_a):
									pkg_link = tds2_a[0]['href']
									pkg_links.append((chn_freq, pkg_link))
								# print chn_freq,pkg_link
							else:continue
					else:
						chn_info = []
						if chn_freq == '':continue
						for td in tds:
							if td.attrs and ('bgcolor','#ffcc99') in td.attrs:chn_info.append(td.text)
							if td.attrs and ('bgcolor','#99ff99') in td.attrs:chn_info.append(td.text)
						if len(chn_info):
							chn_sid_content = chn_info[3]
							chn_sid = chn_sid_content.replace('&nbsp;','').replace(' ','')
							# print chn_info
							if chn_sid and int(chn_sid) == int(sid):chn_name = chn_info[0]
		if chn_name == '':
			if chn_freq == '': return (False, 'No freq found')
			else:
				for link in pkg_links:
					(result, chn_name) = self.lookup_chn_in_pkg(link[1],link[0], sid)
					if result:return (True, chn_name)
				return (False, 'No sid found')
		return (True, chn_name)

	# 在package页面中查找指定freq上指定sid的频道
	def lookup_chn_in_pkg(self, url, freq, sid):
		logger.info('=> Parsing %s %s %s' % (url,freq,sid))
		chn_name = ''
		chn_freq = ''
		pkg_link = ''
		try:
			html_doc = self.get_page_contents(url)
			if html_doc == '':return (False, 'url open failed')
			soup = BeautifulSoup(html_doc)
		except Exception, e:
			ex = sys.exc_info()
			logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
			return (False, 'url parse failed')

		tables = soup.findAll('table', width='720')
		if len(tables) > 1:
			# print 'table num:',len(tables)
			for i in range(0, len(tables)):
				if chn_freq != '':break
				try:
					trs = tables[i].findAll('tr')
				except Exception, e:
					ex = sys.exc_info()
					logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
					break
				for tr in trs:
					tds = tr.findAll('td')
					# first line of a chn_freq
					if len(tds) == 10 and len(tds[0].text) > 2:
						try:
							chn_freqs = tds[0].findAll('b')
						except Exception, e:
							ex = sys.exc_info()
							logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
							break
						chn_freq_content = ''
						if len(chn_freqs) > 0:
							chn_freq_content = chn_freqs[0].text
							chn_freq_content = chn_freq_content.replace('&nbsp;','').strip().split(' ')[0]
						# it's what we need
						if chn_freq_content:
							if chn_freq and float(chn_freq_content) != float(chn_freq):break
							if float(chn_freq_content)== float(freq):
								chn_freq = str(chn_freq_content)
								chn_sid_content = tds[6].text
								chn_sid = chn_sid_content.replace('&nbsp;','').replace(' ','')
								if chn_sid and int(chn_sid) == int(sid):
									chn_name = tds[2].text
									break
							else:continue
					elif len(tds) == 9:
						chn_info = []
						if chn_freq == '':continue
						for td in tds:
							if td.attrs and ('bgcolor','#ffcc99') in td.attrs:
								chn_info.append(td.text)
							if td.attrs and ('bgcolor','#99ff99') in td.attrs:
								chn_info.append(td.text)
						if len(chn_info):
							chn_sid = chn_info[4].lstrip('&nbsp;')
							# print chn_info
							if chn_sid == '':continue
							if chn_sid == sid:
								chn_name = chn_info[0]
								break
		if chn_name == '':
			if chn_freq == '': return (False, 'No freq found')
			else:return (False, 'No sid found')
		return (True, chn_name)

	# 找所有卫星的页面链接
	def get_sat_urls(self, url):
		# print url
		links = []
		try:
			html_doc = self.get_page_contents(url)
			if html_doc == '':return []
			soup = BeautifulSoup(html_doc)
		except Exception,e:
			ex = sys.exc_info()
			logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
			return []
		tables = soup.findAll('table', width='720', align='center')
		if len(tables):
			for table in tables:
				tabs = table.findAll('table')
				for tab in tabs:
					try:
						trs = tab.findAll('tr')
						for tr in trs:
							tds = tr.findAll('td')
							if len(tds) == 4:
								sdg_content = tds[1].text
								sdg = '%s%s' % (sdg_content.strip().strip('&nbsp;').split('&')[0],sdg_content.strip().strip('&nbsp;').split(';')[-1])
								alinks = tds[1].findAll('a')
								alink = alinks[0]['href']
								link = (sdg, alink)
								links.append(link)
					except Exception, e:
						ex = sys.exc_info()
						logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
		return links

	# 读取所有卫星的页面链接
	def get_sat_links(self):
		links = []
		if os.path.exists('satelliteUrls.txt'):
			# print 'reading satellite urls from file...'
			file_sat_url = open('satelliteUrls.txt', 'r')
			for line in file_sat_url.readlines():
				links.append(tuple(eval(line.encode())))
			file_sat_url.close()
		else:
			# print 'reading satellite urls from lyngsat.com...'
			url_file = open('lyngsatUrls.txt', 'r')
			links_return = []
			for url in url_file.readlines():
				links_return.extend(self.get_sat_urls(url))
			url_file.close()
			file_sat_url = open('satelliteUrls.txt', 'w')
			for link in links_return:
				if link not in links:
					links.append(link)
					file_sat_url.write('%s\n' % str(link).decode())
			file_sat_url.close()
		return links

	# 卫星degree数值与方向转换
	def sat_num_to_dir(self, sat_num):
		sat_num = int(sat_num)
		sdgDir = 'E'
		if sat_num > 1800:
			sdgDir = 'W'
			sat_num = 3600 - sat_num
		sdgNum = sat_num/10
		sat_dir = '%0.1f%s' % (sdgNum, sdgDir)
		return sat_dir

	def get_page_contents(self, url):
		page_contents = ''
		file_path = './satellitePages/sat_' + str(hash(url)) + '_' + url.split('/')[-1]
		if os.path.exists(file_path):
			# print 'reading page contents from file...'
			file_page = open(file_path, 'r')
			page_contents = file_page.read()
			file_page.close()
		else:
			# print 'reading page contents from lyngsat.com...'
			if not os.path.exists('./satellitePages'):os.makedirs('./satellitePages')
			try:
				res = urllib2.urlopen(url, timeout=20)
				page_contents = res.read()
			except Exception,e:
				ex = sys.exc_info()
				logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
				return ''
			try:
				file_sat_url = open(file_path, 'w')
				file_sat_url.write(str(page_contents))
				file_sat_url.close()
			except Exception,e:
				ex = sys.exc_info()
				logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
				if os.path.exists(file_path):os.remove(file_path)

		return page_contents

	# 根据udp生成的列表文件查找所有信息
	def gen_all_name(self, from_file, to_file):
		if not os.path.exists(from_file): return
		f = open(from_file, 'r')
		file_chn = open(to_file, 'w')
		logger.info('-'*10 + 'sid' + '-'*10 + 'sfq' + '-'*10 + 'sdg' + '-'*10 + 'sname' + '-'*10 + '\n')

		for line in f.readlines():
			chn_f = eval(line)
			sdg = self.sat_num_to_dir(chn_f['sdg'])
			sfq = chn_f['sfq']
			sid = chn_f['sid']
			sname = 'No dgr found'
			try:
				urls_sats =  lyngsat.lookup_sat_urls(sdg)
				for urls_sat in urls_sats:
					(result,sname) = self.lookup_chn_in_sat(urls_sat, sfq, sid)
					if result:break
			except Exception, e:
				ex = sys.exc_info()
				logger.info('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
				sname = 'None'
			chn_info = '%s, %s, %s, %s' % (sid, sfq, sdg, sname)
			try:
				file_chn.write('%s\n' % chn_info.encode('utf-8'))
			except Exception, e:
				ex = sys.exc_info()
				logger.warning('Exception \"%s\" in line %d' % (ex[1], ex[2].tb_lineno))
			logger.info(chn_info + '\n')
		logger.info('-'*10 + 'sid' + '-'*10 + 'sfq' + '-'*10 + 'sdg' + '-'*10 + 'sname' + '-'*10)
		file_chn.close()
		f.close()

def sort_sat_by_freq():
	f = open('satellites.txt', 'r')
	file_chn = open('satellitess.txt', 'w')

	sats = []
	for line in f.readlines():
		sat = eval(line)
		sat_dg = sat['sdg']
		sat_fq = sat['sfq']
		sat_id = sat['sid']
		sats.append((sat_dg, sat_fq, sat_id))
	sats = sorted(sats, key=lambda sat: sat[1])

	for sat in sats:
		chn_info = {'sdg': sat[0], 'sfq': sat[1], 'sid': sat[2]}
		file_chn.write('%s\n' % str(chn_info).encode('utf-8'))
	file_chn.close()
	f.close()

def config_logging(do_log):
	if not do_log:return MyLogging()
	# 配置日志信息
	logging.basicConfig(level=logging.DEBUG,
						format='%(message)s',
						datefmt='%m-%d %H:%M',
						filename='lyngsat.log',
						filemode='w')
	# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
	console = logging.StreamHandler()
	console.setLevel(logging.INFO)
	# 设置日志打印格式
	formatter = logging.Formatter('%(message)s')
	console.setFormatter(formatter)
	# 将定义好的console日志handler添加到root logger
	logging.getLogger('').addHandler(console)
	logger = logging.getLogger('as_channel')
	return logger

if __name__ == '__main__':
	logger = config_logging(0)
	lyngsat = Lyngsat()


	# print 'asia.html:',len(lyngsat.get_sat_urls('http://www.lyngsat.com/asia.html'))
	# print lyngsat.get_chn_urls('http://www.lyngsat.com/Telstar-18.html')
    #
	# links = lyngsat.get_sat_links()
	# print 'we have %s links to parse.' % len(links)
    #
	# sort_sat_by_freq()
	# print lyngsat.get_page_contents('http://www.lyngsat.com/Astra-1KR-1L-1M-1N.html')

	# exit()

	urls_sats =  lyngsat.lookup_sat_urls('13.0E')
	for urls_sat in urls_sats:
		(result, chn_name) = lyngsat.lookup_chn_in_sat(urls_sat, 10758, 17022)
		if result:break
	logger.info('chn name:' + chn_name)

	exit()

	# sort_sat_by_freq()
	lyngsat.gen_all_name('satellites.txt', 'channels.txt')