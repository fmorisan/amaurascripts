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
import csv # dan learn from this pl0x


progname = '8ball'

def main(args):
	random.seed() 
	slot1 = random.randint(1,12)  
	slot2 = random.randint(1,12) 	
	slot3 = random.randint(1,12) 
	slot1c = content(slot1)
	slot2c = content(slot2)
	slot3c = content(slot3)
	pp = open("/home/skype/pp") #open pp
	ppLines = pp.readlines() #make pp a variable
	ppString = "".join(ppLines) #make the variable a string
	userName = re.compile("(?<="+os.environ["SKYPE_USERNAME"]+"¶)[0-9]+") #compile the entry-searcher
	match = userName.search(ppString) #find the first match for the entry
	pp.close()
	if match:
		userpp = match.group(0)
		userpp = int(userpp)
		userpp = userpp - 10
		if userpp < 0:
			print "Sorry, you dont have enough pp to play this game.. Do !playosu first or something."
			return
		print("You put 10pp into the slots machine...")
		print(slot1c + "   " + slot2c + "   " + slot3c )
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
		with open("/home/skype/pp", "w") as newfile:
			newUserpp = str(newUserpp)
			newfileString = re.sub("(?<="+os.environ["SKYPE_USERNAME"]+"¶)[0-9]+", newUserpp, ppString)
			newfile.write(newfileString)
	else:
		with open("/home/skype/pp", "a+") as file2:
			file2.write(os.environ["SKYPE_USERNAME"]+"¶100 \n")
			print "Welcome to osu! You have been registered automatically, and 100pp have been added to your account. You can obtain more by playing osu (!playosu) or by begging other people to give you some!"
			file2.close
			return
	
def content(number):
	if number == 1:
		return ":]"
	elif number == 2:
		return ":["
	elif number == 3:
		return ":|"
	elif number == 4:
		return ":>"
	elif number == 5:
		return ":<"
	elif number == 6:
		return ":O"
	elif number == 7:
		return ":7"
	elif number == 8:
		return "B)"
	elif number == 9:
		return ":U"
	elif number == 10:
		return ":s"
	elif number == 11:
		return "D:"	
	elif number == 12:
		return ":D"
if __name__ == '__main__':
	main(sys.argv[1:])
