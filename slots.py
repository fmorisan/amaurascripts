#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An 8ball module
"""
import sys #import sys (why?)
import re #import regex
import os #import os (why?)
import time
import random
import sharedVars
import ppHelp

progname = '8ball'

def main(args):
	content = [":]",":[",":|",":>",":<",":O",":7","B)",":U",":s","D:",":D"]
	random.seed()
	slot1c = content[random.randint(0,11)]
	slot2c = content[random.randint(0,11)]
	slot3c = content[random.randint(0,11)]
	with open(sharedVars.ppPath, "r") as ppFile:
		ppJson = json.load(ppFile)
	if sharedVars.username in ppJson:
		userpp = ppJson[username]
		if userpp < 0:
			print "Sorry, you dont have enough pp to play this game.. Do !playosu first or something."
			return
		userpp = userpp - 10
		print("You put 10pp into the slots machine...")
		print(slot1 + "   " + slot2 + "   " + slot3 )
		if slot1 == slot2 and slot2 == slot3:
			if slot1 == 7:
				print("SUPER JACKPOT!!") 
				print("You've won 750pp!!!")
				newUserpp = userpp + 750
			else:
				print("JACKPOT!!") 
				print("You've won 50pp!!")
				newUserpp = userpp + 50
		elif slot1 == slot2:
			print("DING! DING! DING!")
			print("We have a winner!")
			print("You gained 20pp!!")
			newUserpp = userpp + 20		
		elif slot2 == slot3:
			print("DING! DING! DING!")
			print("We have a winner!")
			print("You gained 20pp!!")
			newUserpp = userpp + 20
		elif slot1 == slot3:
			print("DING! DING! DING!")
			print("We have a winner!")
			print("You gained 20pp!!")
			newUserpp = userpp + 20
		elif slot1 == 7 or slot2 == 7 or slot3 == 7:
			print("Consolation prize!")
			print("You get your pp back!")
			newUserpp = userpp + 10
		else:
			print("You lost! :(")
			newUserpp = userpp
		print "Total pp: " + str(newUserpp)
	else:
		ppHelp.register(sharedVars.username, ppJson)

if __name__ == '__main__':
	main(sys.argv[1:])
