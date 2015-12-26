#!/usr/bin/env python

from socket import *
from time import ctime
import MySQLdb

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

	cxn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='dbtest',port=3306)
	cur = cxn.cursor()

	while not exitScript:
		data = tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		if data == '#quit':
			exitScript = True
			break
		result = cur.execute('INSERT INTO chipsn SET chipsn="' + data + '"')
		tcpCliSock.send('[%s] %s, %s affected' % (ctime(), data, result))
	cur.close()
	cxn.commit()
	cxn.close()
	tcpCliSock.close()
tcpSerSock.close()