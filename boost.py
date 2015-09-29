#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import sys #import sys (why?)
import json
import os #import os (why?)
import sharedVars
import ppHelp
	


def main(args): #define main program body
	"""The program entry point."""
	
	

	
	if args:
		if args[0] == "help":
			ppHelp.helpText()
		elif len(args) == 2:
			target = args[1]
			amount = int(args[0])
			with open(sharedVars.ppPath, "r") as ppFile: #open pp
				ppJson = json.load(ppFile)
			if sharedVars.username in ppJson:
				if target in ppJson:
					if ppJson[sharedVars.username] >= sharedVars.boostCost+amount:
						ppJson[sharedVars.username] = (ppJson[sharedVars.username] - sharedVars.boostCost) - amount
						ppJson[target] = ppJson[target] + amount
						with open(sharedVars.ppPath, "w") as ppFile:
							json.dump(ppJson,ppFile,indent=1)
						print "{} has given {} {}pp!".format(sharedVars.alias,target,amount)
					else:
						print "Sorry, you can't afford that! (Remember this service costs {} extra pp to use.)".format(sharedVars.boostCost)
				else:
					print "Sorry, the target is not registered."
			else:
				ppHelp.register(sharedVars.username, ppJson)
				
		else:
			ppHelp.helpText()
	else:
		ppHelp.helpText()

if __name__ == "__main__": #wat
    main(sys.argv[1:]) #call main program body.