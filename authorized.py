
"""
A simple sample module with command authorization testing
and some useful functions
"""
import sys
import os
import time
#import yaml
import json
from sharedVars import authorizedPath



def isAuth(username):
	with open(authorizedPath) as file:
		auths = json.load(file)
	if username not in auths: return False
	else: return auths[username]
		
def authorized(username): #still here for legacy support
	ops = open("/home/skype/oplist.txt", "r").readlines()
	l = list()
	for name in ops:
		l.append(name.strip())
	return username in l

def import_users(path):
	f = open(path)
	lines = f.readlines()
	f.close()
	lines = "".join(lines)
	#return yaml.safe_load(lines)

