#!/usr/bin/env python

from socket import *
from time import ctime
import json
import MySQLdb
import string

HOST = '192.168.0.156'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
exitScript = False

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while not exitScript:
	print 'waiting for connection...'
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connected from: ', addr



	while not exitScript:
		data = tcpCliSock.recv(BUFSIZ)
		if data == '#quit':
			exitScript = True
			tcpCliSock.send('#quit')
			break

		print type(data)
		print data
		if isinstance(data, str):
			# data = data[1:-1]
			if data == '{"chipid": "e43834ed52020000","hw": "00170001","sw": "0063.0011"}':
				print "===== is equal ====="
			dataDict = json.loads(data)
			print type(dataDict)
			chipid = dataDict['chipid']
			hw = dataDict['hw']
			sw = dataDict['sw']
		elif isinstance(data, dict):
			chipid = data['chipid']
			hw = data['hw']
			sw = data['sw']
		else:
			break

		cxn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='dbtest',port=3306)
		cur = cxn.cursor()

		try:
			queryString = 'INSERT INTO chipsn SET chipsn="' + chipid + '",hw="' + hw + '",sw="' + sw + '"'
			print queryString
			result = cur.execute(queryString)
			tcpCliSock.send('[%s] %s, %s affected' % (ctime(), data, result))
		except Exception, e:
			print 'MySQL execute error!'
			tcpCliSock.send('[%s] %s' % (ctime(), e))
			print e
		else:
			pass
		finally:
			pass


		
		cur.close()
		cxn.commit()
		cxn.close()

	tcpCliSock.close()
tcpSerSock.close()