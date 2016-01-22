#!/usr/bin/env python
# python channelsName.py 104.236.146.165 6008

from __future__ import division
from socket import *
from time import ctime
import binascii
import sys
import string
import time

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

satellites = []
timeStart = time.time()
print 'time:',timeStart
f = open('satellites.txt', 'w')
secondsGo = 600

print 'waiting for message...'
while True:
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	data = binascii.hexlify(data)
	# print 'received \"%s\" from %s' % (data, addr)
	sdgs = int(data[0:4], 16)
	sfqs = int(data[4:8], 16)
	sids = int(data[8:12], 16)

	if sdgs > 1800:
		sdgDir = 'W'
		sdgNum = 3600 - sdgs
	else:
		sdgDir = 'E'
		sdgNum = sdgs
	sdgNum = sdgNum/10

	sate = {'sid':sids, 'sfq':sfqs, 'sdg':sdgs}

	if sate not in satellites:
		satellites.append(sate)
		print 'degree: %0.1f%s, fq: %d, sid: %d, data: %s' % (sdgNum, sdgDir, sfqs, sids, data)
		f.write('%s\n' % sate)
	
	timeNow = time.time()
	timeGo = timeNow - timeStart
	if timeGo > secondsGo:
		#print satellites.values()
		break

f.close()
udpSerSock.close()
