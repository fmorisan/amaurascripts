#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test module to send commands to the server via skype.
"""
import os
import sys
import sharedVars
from authorized import isAuth
progname = 'umodule'

def main(args):
	if args:
		if len(args) == 2:
			if isAuth(sharedVars.username) == 3:
				modname = args[0]
				link = args[1]
				os.system('wget -nv -O ~/sevabot/modules/' + modname + '.py \'' + link + '\'')
				os.system('chmod +x ~/sevabot/modules/' + modname + '.py')
				return
			else:
				print 'You\'re not authorized to use this command.'
				return
		else:
			print 'Syntax error.'
			print 'Usage: !umodule (module) (direct link)'
			return
	else:
		print 'Syntax error.'
		print 'Usage: !umodule (module) (direct link)'
		return

if __name__ == '__main__':
	main(sys.argv[1:])
