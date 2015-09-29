#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An 8ball module
"""
import sys
import random

progname = '8ball'

def main(args):



	random.seed() 


        if "again" in args:
        	print "Ask again."
        	sys.exit()
	if "maeg" in args:
		print "maeg sux."
		sys.exit()
	rand1 = random.randint(1,8)
	rand2 = 1
	if rand1 == 1:
		print 'Yes.'
		return
	elif rand1 == 2:
		print 'No.'
		return
	elif rand1 == 3:
		print 'Maybe.'
		return
	elif rand1 == 4:
		print 'Ask again.'
		return
	elif rand1 == 5:
		print 'Questions that meddle with the dark arts will be ignored.'
		return
	elif rand1 == 6:
		print "I don't know."
		return
	elif rand1 == 7:
		print 'Ask Loctav.'
		return
	elif rand1 == 8:
		print 'Hell naw.'
		return	      
	return


if __name__ == '__main__':
	main(sys.argv[1:])
