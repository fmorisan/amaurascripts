#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import sys
import os 
import json
import sharedVars
import ppHelp

def main(args): #define main program body

	if args:
		ppHelp.helpText()
	else:
		with open(sharedVars.ppPath, "r") as ppFile:
			ppJson = json.load(ppFile)
		if sharedVars.username in ppJson:
			

			if ppJson[sharedVars.username] >= 0 and ppJson[sharedVars.username] < 200:
				print "You (" + sharedVars.alias + ") have only " + str(ppJson[sharedVars.username]) + "pp. What a scrublord." #show it to the user
			if ppJson[sharedVars.username] >= 200 and ppJson[sharedVars.username] < 600:
				print "You (" + sharedVars.alias + ") have " + str(ppJson[sharedVars.username]) + "pp. Not so bad, but still bad." #show it to the user
			if ppJson[sharedVars.username] >= 600 and ppJson[sharedVars.username] < 1000:
				print "You (" + sharedVars.alias + ") have " + str(ppJson[sharedVars.username]) + "pp. You're decent!" #show it to the user
			if ppJson[sharedVars.username] >= 1000 and ppJson[sharedVars.username] < 3000:
				print "Wow! You (" + sharedVars.alias + ") have a whopping amount of " + str(ppJson[sharedVars.username]) + "pp! Noice!" #show it to the user
			if ppJson[sharedVars.username] >= 3000:
				print "Incredible! You (" + sharedVars.alias + ") have " + str(ppJson[sharedVars.username]) + "pp. New cokiez confirmed xd" #show it to the user
		else:
			ppHelp.register(sharedVars.username, ppJson)
			

if __name__ == "__main__": #wat
    main(sys.argv[1:]) #call main program body.
