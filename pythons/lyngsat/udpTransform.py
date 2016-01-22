#!/usr/bin/env python

from socket import *
from time import ctime
import binascii

HOST = '46.166.129.193'
PORT = 6000
BUFSIZ = 22
ADDR = (HOST, PORT)

clientHost = '104.236.146.165'
addrClient = (clientHost, 6008)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

print '\nwaiting for message...'
while True:
	data, addrServer = udpSerSock.recvfrom(BUFSIZ)
	print '\n\"%s\"' % binascii.hexlify(data)
	udpCliSock.sendto(data, addrClient)
	print '...received from \"%s\" and returned to \"%s\"' % (addrServer[0], clientHost)

udpSerSock.close()
