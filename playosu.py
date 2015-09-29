#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import sys #import sys (why?)
import os #import os (why?)
import time
import random
import csv # dan learn from this pl0x

import json #swag
import sharedVars #extra swag
import ppHelp #i can't even hold all this swag

def roll(ppJson):
	loss = random.randint(0, ppJson[sharedVars.username]/2)
	gain = random.randint(0,100)
	newUserpp = ppJson[sharedVars.username] + gain - loss
	if newUserpp < 0:
		newUserpp = 0
	if newUserpp > ppJson[sharedVars.username]:
		ppDiff = newUserpp - ppJson[sharedVars.username]
		if ppDiff >= 0 and ppDiff < 10:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " FCs a 250 bpm map with DT and gets " + ppDiff + "pp.",
		if ppDiff >= 10 and ppDiff < 30:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " plays a map nomod and gains " + ppDiff + "pp.",
		if ppDiff >= 30 and ppDiff < 50:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " plays a map with HR and obtains " + ppDiff + "pp.",
		if ppDiff >= 50 and ppDiff < 80:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " plays a DT map and gains " + ppDiff + "pp.",
		if ppDiff >= 80 and ppDiff < 100:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " plays a DT TV Size and gains " + ppDiff + "pp.",
	else:
		ppDiff = ppJson[sharedVars.username] - newUserpp
		if ppDiff >= 0 and ppDiff < 10:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " plays a 7 star map and loses " + ppDiff + "pp.",
		elif ppDiff >= 10 and ppDiff < 30:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " plays a map nomod but gets shit accuracy and loses " + ppDiff + "pp.",
		elif ppDiff >= 30 and ppDiff < 50:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " plays a map with HD and passes a HR score, losing " + ppDiff + "pp.",
		elif ppDiff >= 50 and ppDiff < 80:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " passes a DT score with HDHR and loses " + ppDiff + "pp.",
		elif ppDiff >= 80 and ppDiff < 100:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " gets robbed by RLC and loses " + ppDiff + "pp.",
		elif ppDiff >= 100:
			ppDiff = str(ppDiff)
			print sharedVars.alias + " loses " + ppDiff + "pp due to a formula change.",
	print "Total: " + str(newUserpp)
	with open(sharedVars.ppPath, "w") as ppFile:
		ppJson[sharedVars.username] = newUserpp
		json.dump(ppJson,ppFile,indent=1)
	return	
			
			
def main(args): #if swag == over.9000:
	"""The program entry point."""
	with open(sharedVars.ppPath, "r") as ppFile: #open pp
		ppJson = json.load(ppFile) #reading them json
	if sharedVars.username in ppJson: #is this motherfucked registered
		with open(sharedVars.inventoryPath, "r") as inventoryFile:
			invJson = json.load(inventoryFile)
	if args:

		if args[0] == "help":
			ppHelp.helpText() #sick 360 camelCase
		if args[0] == "aon":

				maxrange = 33
				if sharedVars.username in invJson:
					if "5%ext" in invJson[sharedVars.username]:
						maxrange += 5
					if "5%ext2" in invJson[sharedVars.username]:
						maxrange += 5 
				aon = random.randint(1,100)
				if aon in range(1,maxrange):
					newPp = ppJson[sharedVars.username] + ppJson[sharedVars.username]
				else:
					newPp = 0
				if newPp > ppJson[sharedVars.username]:
					ppDiff = str(newPp - ppJson[sharedVars.username])
					print sharedVars.alias + " has gained " + ppDiff + "pp.",
				else:
					ppDiff = str(ppJson[sharedVars.username] - newPp)
					print sharedVars.alias + " has lost " + ppDiff + "pp.",
				with open(sharedVars.ppPath, "w") as ppFile:			
					ppJson[sharedVars.username] = newPp
					json.dump(ppJson,ppFile,indent=1)

	else:
		with open(sharedVars.ppPath, "r") as ppFile: #open pp
			ppJson = json.load(ppFile)
		if sharedVars.username in ppJson:
			roll(ppJson)
			if sharedVars.username in invJson:
				if "double_roll" in invJson[sharedVars.username]:
					roll(ppJson)	

		else:
			ppHelp.register(sharedVars.username, ppJson)

if __name__ == "__main__": 
    main(sys.argv[1:]) 
