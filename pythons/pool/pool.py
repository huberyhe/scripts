#!/usr/bin/env python

from multiprocessing import Pool, TimeoutError
import time
import os, sys
import random

def f(x):
	time.sleep(2*random.random())
	return x*x

def p(t):
    print '%03d\r' % (t, ),
    sys.stdout.flush()

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes

    # print "[0, 1, 4,..., 81]"
    print pool.map(f, range(10))

    # print same numbers in arbitrary order
    for i in pool.imap_unordered(f, range(10)):
        print i, '\r',

    # evaluate "f(20)" asynchronously
    res = pool.apply_async(f, (20,))      # runs in *only* one process
    print res.get(timeout=2)              # prints "400"

    # evaluate "os.getpid()" asynchronously
    res = pool.apply_async(os.getpid, ()) # runs in *only* one process
    print res.get(timeout=1)              # prints the PID of that process

    # launching multiple evaluations asynchronously *may* use more processes
    multiple_results = [pool.apply_async(f, (v, ), callback=p(i)) for i,v in enumerate([0, 1, 4, 9, 16, 25, 36, 49, 64, 81])]
    print '---'
    print [res.get(timeout=2) for res in multiple_results]
    print '==='

    # make a single worker sleep for 10 secs
    res = pool.apply_async(time.sleep, (10,))
    try:
        print res.get(timeout=1)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"

    print '\33[?25l'
    for i in range(10):
    	time.sleep(1)
    	print '%02d/%2d\r' % (i, 10),
    	sys.stdout.flush()
    print '\33[?25h'

    for i, v in enumerate([0, 1, 4, 9, 16, 25, 36, 49, 64, 81]):
    	print i, v