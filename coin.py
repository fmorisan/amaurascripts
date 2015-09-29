#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An 8ball module
"""
import sys
import random

progname = 'coin'

def main(args):



	random.seed() 


           
	rand1 = random.randint(1,2)
	if rand1 == 1:
		print 'Heads'
		return
	elif rand1 == 2:
		print 'Tails'
		return
	return


if __name__ == '__main__':
	main(sys.argv[1:])
