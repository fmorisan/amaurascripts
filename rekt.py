#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test module to send commands to the server via skype.
"""
import os
import sys
import random
progname = 'rekt'

def main(args):
	lines = [line.rstrip() for line in open("/home/skype/rektlines.txt", "r").readlines()]
	try:
		n = int(args[0]) - 1
	except Exception: # args[0] was nonexistent or not an integer
		random.seed()
		n = random.randint(0, len(lines)-1)
	finally: # do this anyway
		try:
			assert n in range(len(lines))
			print lines[n]
		except Exception, e: # these fuckers went outside of the range
			print "Please choose a number between 1 - ", len(lines)
if __name__ == '__main__':
	main(sys.argv[1:])
