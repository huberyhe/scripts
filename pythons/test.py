#!/usr/bin/env python
s = 'abcde'
for i in [None] + range(-1, -len(s), -1):
	print s[:i]
