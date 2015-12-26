#!/usr/bin/env python

from socket import *
from time import ctime
import MySQLdb
import threading
import time
import sys

class timer(threading.Thread): #The timer class is derived from the class threading.Thread
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False  
        self.HOST = ''
        self.PORT = 21567
        self.BUFSIZ = 1024
   
    def run(self): #Overwrite run() method, put what you want the thread do here
		ADDR = (self.HOST, self.PORT)
		cxn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='dbtest',port=3306)
		cur = cxn.cursor()
		tcpSerSock = socket(AF_INET, SOCK_STREAM)
		tcpSerSock.bind(ADDR)
		tcpSerSock.listen(5)

		while not self.thread_stop:
			print 'waiting for connection...'
			tcpCliSock, addr = tcpSerSock.accept()
			print '...connected from: ', addr
			while not self.thread_stop:
				data = tcpCliSock.recv(self.BUFSIZ)
				if not data:
					break
				if data == "quit":
					self.thread_stop = True
				queryString = 'INSERT INTO chipsn SET chipsn="' + data + '"'
				print queryString
				result = cur.execute(queryString)
				tcpCliSock.send('[%s] %s, %s affected' % (ctime(), data, result))
				print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())
				time.sleep(self.interval)
			tcpCliSock.close()
		print 'exiting thread...'
		cur.close()
		cxn.commit()
		cxn.close()
		tcpSerSock.close() 
    def stop(self):
    	self.thread_stop = True
         
   
def test():
	tcpThread = timer(1, 1)
	tcpThread.start()
	time.sleep(10)
	exitScript = False
	while not exitScript:
	    data = raw_input('> ')
	    if not data:
	        break
	    if data == "quit":
	    	print 'exiting...'
	    	tcpThread.stop()
	    	exitScript = True
	print "test exited."
	return

if __name__ == '__main__':  
	test()