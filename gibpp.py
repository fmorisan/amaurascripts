#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import sharedVars
import ppHelp
from authorized import authorized

def main(username, ppToAdd):
	if authorized(username):
		with open(sharedVars.ppPath, "r") as ppFile:
			ppJson = json.load(ppFile)
		if username in ppJson:
			try:
				ppJson[username] += ppToAdd
				with open(sharedVars.ppPath, "w") as ppFile:
					json.dump(ppJson, ppFile, indent=1)
			except Exception:
				print "Sorry, something went wrong."
				sys.exit()
		else:
			ppHelp.register(username, ppJson)
	else:
		print "@{}, you're not authorized to use this command.".format(sharedVars.username)

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])