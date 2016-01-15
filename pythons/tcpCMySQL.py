#!/usr/bin/env python

from socket import *
from time import ctime

HOST = '192.168.0.156'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        continue
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if data == "#quit":
        break
    print data

tcpCliSock.close()