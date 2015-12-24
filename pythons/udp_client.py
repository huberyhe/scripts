#!/usr/bin/env python
# UDP Client - udpclient.py
# code by www.cppblog.com/jerryma
import socket, sys
import binascii

HOST = '185.52.2.200'#sys.argv[1]
PORT = 20010 #sys.argv[2]
BUFSIZ = 22
server_address = (HOST, PORT)

message = "aabbcc"
message = binascii.unhexlify(message)
print "message is ", message

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(message, server_address)

gs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
gs_address = ("127.0.0.1", 9200)
gs2_address = ("192.168.2.251", 9200)
while 1:
    data, server = s.recvfrom(BUFSIZ)
    print binascii.hexlify(data)
    #print server
    gs.sendto(data, gs_address)
    #gs.sendto(data, gs2_address)

