#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test module to send commands to the server via skype.
"""
import os
import sys
import subprocess	# new!
progname = 'cmd'

def main(args):
	if args:
		if os.environ["SKYPE_USERNAME"] in ('euphoricradioactivity', 'fmorisan'):
			if not args[0].startswith('sudo'):
				#argss = ' '.join(args)	# List of arguments works now, since we're using subprocess
				#os.system(argss) 		# Same as above.
				exex = subprocess.check_output(args) 	# Create child process, getting ouput as well
				print exex		# That's stdout.
				return
			else:
				print "wat"
				return
		else:
			print 'You\'re not authorized to use this command.'
			return
	else:
		print 'Missing arguments.'
		print 'Usage: !cmd (command)'
		return

if __name__ == '__main__':
	main(sys.argv[1:])
