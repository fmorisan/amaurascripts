#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A roll module
"""
import sys
from random import randint
import re

progname = 'roll'

def default():
	print randint(0,100)


def main(args):
	if args:
		if args[0] == "help": print "Usage: !roll [min] [max]"
		else:
			if len(args) == 1:
				try:
					print randint(0,int(args[0]))
				except: default()
			elif len(args) == 2:
				try:
					print randint(int(args[0]),int(args[1]))
				except: default()
			else: default()
	else: default()

if __name__ == '__main__':
    main(sys.argv[1:])
