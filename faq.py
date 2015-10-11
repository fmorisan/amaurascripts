#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
faq 2.0 (completely rewritten by dan)
"""
import sys 
#import re we don't need this garbage anymore
import os 

from authorized import isAuth
import sharedVars
import json

def printHelp():
	print "Usage:"
	print "!faq add (entry) (content) : Adds an entry to the faq list."
	print "!faq remove (entry) (content) : Removes an entry from the faq list. (Requires an auth level of 1 or higher)"
	print "!faq (entry) : Prints the content of an entry."

def main(args): 
	
	"""it's time for a new swag"""
	
	if args: #if you don't know what this does, get out.
		with open(sharedVars.faq2Path, "r") as faqFile: #open the file, the path is read from sharedVars
			faqList = json.load(faqFile) #load the file as a json
		if args[0] == "remove": 
			if isAuth(sharedVars.username) >= 1: #check for auth using the new auth library
				if len(args) == 2: 
					args[1] = args[1].lower() #entry names are made lowercase to prevent confusion
					if args[1] in faqList: #check if the entry exists
						del faqList[args[1]] #delte it
						with open(sharedVars.faq2Path, "w") as faqFile: #open again
							json.dump(faqList,faqFile,indent=1) #dump json data to file
						print "Succesfully removed entry for {}.".format(args[1]) #tell the user how well we've done
					else: print "Entry not found." 
				else: printHelp() #i put the help test in a function so i could edit it faster
			else: "You're not authorized to use this command." #>2015 >not being auth
		elif args[0] == "add": 
			if len(args) >= 3:
				args[1] = args[1].lower()
				if args[1] not in faqList: #check if the entry *doesn't* exist
					entry = args[1] #then save it to another variable, because...
					del args[0] #delete the first entry in args twice,
					del args[0] #i'm sure there's a better way to do this, but i'm lazy
					content = " ".join(args) #join args into a string
					faqList[entry.lower()] = content #create the entry
					with open(sharedVars.faq2Path, "w") as faqFile:
						json.dump(faqList,faqFile,indent=1) #write to disk
					print "Succesfully added entry for {}.".format(entry)
				else: print "Entry already exists."
			else: printHelp()
		elif args[0] == "list":
			#willPrint = "List of faq entries: "
			#i = 0 ##spaghetti code
			#for entry in faqList: #iterate through every entry in faqList
			#		i += 1 #count how many we've gone through
			#		if i != len(faqList): #check if we're at the end of the list
			#			willPrint = willPrint + entry + ", " #if we aren't, append the entry plus a comma
			#		else:
			#			willPrint = willPrint + entry + "." #if we are, append the entry plus a period instead
			#print willPrint #print the list
			print 'Check out the faq list at http://amaura.tk/faq !!'
		else:
			if len(args) == 1: 
				args[0] = args[0].lower()
				if args[0] in faqList: #if args[0] is in the list of faqs
					print faqList[args[0]] #print it
				else: print "Entry not found." #else, tell the user they're dumb as shit
			else: printHelp()
		
	else:
		printHelp()
if __name__ == "__main__": 
    main(sys.argv[1:])
