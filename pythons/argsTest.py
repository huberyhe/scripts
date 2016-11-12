#!/usr/bin/env python

import os, sys
import getopt

try:
	options,args = getopt.getopt(sys.argv[1:],"hvVc:",["help", "verbose", "keys", "channel="])
except getopt.GetoptError as err:
	print str(err)
	sys.exit(3)

verbose = 0
cmd = 0
res = 0
pfs = [192, 10729, "v", 30819]

if 'servers' in args:
	cmd = 1
if 'services' in args:
	cmd = 2
if 'keys' in args:
	cmd = 3

for name,value in options:
	if name in ("-h","--help"):
		cmd = 0
	if name in ("-v","--verbose"):
		verbose = 1
	if name in ("-V",):
		verbose = 2
	if name in ("-c", "--channel"):
		pfs = list(value)

print "verbose: %d, cmd: %d, pfs: %s" % (verbose, cmd, str(pfs))

sys.exit(0)

if not cmd:
	usage(argc,argv)
	print 'Unknown input.'
	res = 3
else:
	if cmd == 1:
		pass
	elif cmd == 2:
		pass
	else:
		pass