#!/usr/bin/env python

from socket import *
from time import ctime
import sys

HOST = ''
PORT = 0
BUFSIZ = 1024

if len(sys.argv) != 3:
	print "Usage: python %s <ip> <port>"%(sys.argv[0])
	quit()

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])
print "HOST: %s, PORT: %d"%(HOST, PORT)
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print 'waiting for message...'
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	if not data:
		continue
	if "QUIT" in data:
		break
	print 'received \"%s\" from %s' % (data, addr)
	udpSerSock.sendto('[%s] %s' %(
		ctime(), data), addr)
	print '...received from and returned to:', addr

udpSerSock.close()
