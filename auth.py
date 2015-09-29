#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple swag
"""

import sys
import os
import random

import json #swag B)
import authorized
import sharedVars
import authHelp


def main(args):
	if args:
		if args[0] == "help":
			authHelp.helpText()
		elif args[0] == "add":
			if len(args) == 3:
				if authorized.isAuth(sharedVars.username):
					if authorized.isAuth(sharedVars.username) - int(args[2]) > 0:
						if authorized.isAuth(args[1]):
							if not authorized.isAuth(sharedVars.username) == 3 or authorized.isAuth(args[1]) == 3: 
								print "You cannot promote or demote people."
								return				
						with open(sharedVars.authorizedPath) as file:
							auths = json.load(file)
						with open(sharedVars.authorizedPath, "w") as file:
							auths[args[1]] = int(args[2])
							json.dump(auths,file,indent=1)
						print "Succesfully added {} as level {} auth.".format(args[1],args[2])
					else: print "You can't add auths on your own level or higher."
				else: print "You're not authorized to use this command."
			else: authHelp.helpText()
		elif args[0] == "remove":
			if len(args) == 2:
				if authorized.isAuth(sharedVars.username):
					if authorized.isAuth(sharedVars.username) == 3 and authorized.isAuth(args[1]) != 3:
						with open(sharedVars.authorizedPath) as file:
							auths = json.load(file)
						with open(sharedVars.authorizedPath, "w") as file:
							auths[args[1]] = 0
							json.dump(auths,file,indent=1)
						print "{} is no longer an auth.".format(args[1])
					else: print "Insufficient security cleareance. Access denied."
				else: print "You're not authorized to use this command."
		elif args[0] == "check":
			if len(args) == 2:
				if authorized.isAuth(args[1]):
					print "{} is a level {} auth.".format(args[1],authorized.isAuth(args[1]))
				else: print "{} is not an auth.".format(args[1])
		else: authHelp.helpText()
if __name__ == "__main__": 
    main(sys.argv[1:]) 
