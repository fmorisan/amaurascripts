#!/usr/bin/env python

import sys
import random
import sharedVars # use dan's module because we might as well just do it

def main(args):
	summonStrings = ["{}, you have been summoned by {}! GET YO ASS OVER HERE",
			 "{}, please come. It's not like {} wants to talk to you or anything, baaaaka",
			 "{}, {} summoned you. But it's not like they miss you or anything.",
			 "{}, {} has stolen all your pp maps! Get in here and get your peppyronis back!"]
	if len(args) > 0:
		string = " ".join(args)
		rnd = random.randint(0,len(summonStrings)-1)
		print summonStrings[rnd].format(" ".join(args), sharedVars.alias)
	else:
		print "{} summons everyone to the chat!".format(sharedVars.alias)

main(sys.argv[1:])
