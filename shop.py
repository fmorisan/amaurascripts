#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple shopping simulator 2k15
"""
import sys
import os
import time
import random
import csv 
import datetime
import json #swag
import sharedVars #extra swag
import ppHelp #i can't even hold all this swag

def saveChanges(ppJson,invJson):
	with open(sharedVars.ppPath, "w") as ppFile:
		json.dump(ppJson,ppFile,indent=1)
		
	with open(sharedVars.inventoryPath, "w") as invFile:
		json.dump(invJson,invFile,indent=1)

def main(args): #if swag == over.9000:
	"""The program entry point."""
	if args:
		with open(sharedVars.shopPath, "r") as shopFile: #open shop
			shopJson = json.load(shopFile)
		with open(sharedVars.ppPath, "r") as ppFile:
			ppJson = json.load(ppFile)
		with open(sharedVars.inventoryPath, "r") as inventoryFile:
			invJson = json.load(inventoryFile)
		if sharedVars.username in invJson:
			if args[0] == "help":
				ppHelp.helpText() #sick 360 camelCase
			elif args[0] == "list":
				i = 0
				willPrint = "List of shop items: \n"
				for entry in shopJson:
					i += 1
					willPrint = willPrint + entry +": {} Cost: {}pp \n".format(shopJson[entry]["description"],shopJson[entry]["price"])
				print willPrint
			elif args[0] == "buy":
				if args[1] in shopJson:
					item = args[1]
					if ppJson[sharedVars.username] >= shopJson[item]["price"]:
						if item not in invJson[sharedVars.username]:
							ppJson[sharedVars.username] -= shopJson[args[1]]["price"]
							invJson[sharedVars.username][item] = 1
							print "Purchase complete."
							saveChanges(ppJson,invJson)
						else: print "You already have this item."
					else: print "You can't afford this."
				else: print "Item not found."
					
			elif args[0] == "inventory":
				i = 0
				willPrint = "Stuff in your inventory: \n"
				for item in invJson[sharedVars.username]:
					i += 1
					willPrint = willPrint + item +"\n"
				print willPrint
			else:
				ppHelp.helpText()
				
		else:
			invJson[sharedVars.username] = {}
			saveChanges(ppJson, invJson)
			main(args)
	else: ppHelp.helpText()
if __name__ == "__main__": 
    main(sys.argv[1:]) 
