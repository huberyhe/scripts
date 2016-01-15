#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = raw_input('> ')
	if not data:
		continue
	if "QUIT" in data:
		break
	udpCliSock.sendto(data, ADDR)
	data, ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		continue
	if "QUIT" in data:
		break
	print data
udpCliSock.close()
