#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import sys #import sys (why?)
import json
import os
import sharedVars
import ppHelp
def main(args): #define main program body
	"""The program entry point."""
	
	
	
	
	if args:
		if args[0] == "help":
			ppHelp.helpText()
		else:
			with open(sharedVars.ppPath, "r") as ppFile: #open pp
				ppJson = json.load(ppFile)
			if sharedVars.username in ppJson:
				userpp = ppJson[sharedVars.username]
				if userpp >= sharedVars.kickCost:
					newUserpp = userpp - sharedVars.kickCost
					print("/kick " + args[0])
					with open(sharedVars.ppPath, "w") as ppFile:
						newUserpp = str(newUserpp)
						json.dump(ppJson,ppFile,indent=1)
				else:
					print "Sorry Dave, I can't do that."
					print "(You're broke as fuck, this shit costs "+str(sharedVars.kickCost)+" pp, go play some osu)"
				
			else:
				ppHelp.register(sharedVars.username,ppJson)
	else:
		ppHelp.helpText()

if __name__ == "__main__": #wat
	#main(sys.argv[1:]) #call main program body.
	sys.exit()