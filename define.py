#!/usr/bin/env python
# -*- coding:utf-8 -*-
#####
# A simple dictionary API call for definition requests
#####
import sys
import unirest
import json
# These code snippets use an open-source library. http://unirest.io/python
try:
	query = " ".join(sys.argv[1:]).lower()
	response = unirest.get("https://montanaflynn-dictionary.p.mashape.com/define?word=" + query, headers={"X-Mashape-Key": "FKEW3Xem46mshjH0UAHsW1EIuodkp1mVFOSjsnQm20z3pZZO7c","Accept": "application/json"})
	response = response.body["definitions"]

	if len(response) < 1:
		print "Word not found! Did you make a typo?"
		raise Exception
	print "Definition for {}.".format(query)
	if 2 < len(response):
		k = 2
	else:
		k = len(response)
	for x in range(k):
		print u"{}. {}".format(x+1, response[x]["text"])
except Exception, e:
	pass
#	print repr(e)
finally:
	pass
