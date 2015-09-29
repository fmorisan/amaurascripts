#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Looks arguments up on bloodcat **TEST**
"""
import sys
import os
import re
from string import ascii_letters, digits
progname = 'bc'

def main(args):
	argss = ' '.join(args)
	if argss == 'help':
		print 'This command returns the first result for a bloodcat query.'
		print 'Usage: \"!bc (query)\" or \"!bloodcat (query)\"'
		return
	else:
		argsp = ' '.join(args)
		for char in argsp:
			if char not in (ascii_letters + digits):
				if char == ' ':
					argsp = argsp.replace(char, '+')
				else:
					argsp = argsp.replace(char, '')
		os.system('wget --quiet  -O ~/tempbc/t.html  \'http://bloodcat.com/osu/?q=' + argsp + '&m=b&c=&g=&d=&s=title&o=1\'')
		f=open('/home/skype/tempbc/t.html')
		lines=f.readlines()
		rline = lines[23]
		#print rline
		rlink = re.search('s/[0-9]+', rline)
		rname = re.search ('(?<=">)[^<^>.]+(?=.*[>]$)', rline)
		rartist = re.search ('(?<=</a><br>)[^<^>.]+(?=.*[>]$)', rline)
		rmapper = re.search ('(?<=u">)[^<^>.]+(?=.*[>]$)', rline)
		if rname:
			print 'http://bloodcat.com/osu/' + rlink.group(0) + '  ' + rname.group(0) + ' - ' + rartist.group(0) + ' (Mapped by ' + rmapper.group(0)  + ')'
		else:
			print 'No results found.'
		os.system('rm ~/tempbc/t.html')
		return

if __name__ == '__main__':
    main(sys.argv[1:])
