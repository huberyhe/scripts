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

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	data = raw_input('> ')
	if not data:
		continue
	udpCliSock.sendto(data, ADDR)
	if "QUIT" in data:
		break
	data, ADDR = udpCliSock.recvfrom(BUFSIZ)
	if not data:
		continue
	if "QUIT" in data:
		break
	print data
udpCliSock.close()
