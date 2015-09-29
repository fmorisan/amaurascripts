#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test module to send commands to the server via skype.
"""
import os
import sys
from authorized import authorized
progname = 'source'

def main(args):
	if args:
		#os.system('puush ~/sevabot/modules/' + args[0] + '.py')
		if os.path.exists("/home/skype/sevabot/modules/"+args[0]+".py") or os.path.exists("/home/skype/sevabot/modules/"+args[0]+".sh"):
			print "http://amaurabot.tk/mod/modules/" + args[0] + ".py"
			return
		else:
			print "Module " + args[0] + " doesn't exist."
	else:
		print 'Missing arguments.'
		print 'Usage: !source (module)'
		return

if __name__ == '__main__':
	main(sys.argv[1:])
