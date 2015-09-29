#!/usr/bin/env python

import random, sys
import math
#import numpy

def deviation(l):
	# find the mean value
	mean = 0
	for k in l:
		mean += k
	mean /= len(l)

	# find sum
	sum = 0
	for k in l:
		sum += (k - mean)**2
	
	# mult by 1/n - 1
	dev = float(1)/(len(l) - 1)*sum
	dev = math.sqrt(dev)

	#return
	return dev

try:
	x = int(sys.argv[1])
	assert x > 1
except:
	x = 1
	print "Defaulted to 1 dice roll."

random.seed()

reslist = list()

for k in range(x):
	reslist.append(random.randint(1,10))
clist = list()

for k in range(1,11):
	counter = 0
	for j in range(len(reslist)):
		if reslist[j] ==  k:
			counter += 1
	print k, "was rolled", counter, "times.", str(100*float(counter)/x)+"%"
	clist.append(counter)

if "s" in sys.argv:
	print "Std. Deviation for this roll was:", deviation(clist)
