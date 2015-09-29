#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Looks arguments up on bloodcat **TEST**
"""
import sys
import os
import re
progname = 'bm'

def main(args):
	argss = ' '.join(args)
	if argss == 'help':
		print 'This command returns the first result for an osu! beatmap query.'
		print 'Usage: \"!bm (query)\" or \"!beatmap (query)\"'
		print 'WARNING: THIS COMMAND DOES NOT SUPPORT APOSTROPHES.'
		return
	else:
		argsp = argss.replace(' ', '+')
		os.system('wget --quiet  -O ~/tempbc/t2.html  \'http://osu.ppy.sh/p/beatmaplist?q=' + argsp + '&m=-1&r=0&g=0&la=0\'')
		f=open('/home/skype/tempbc/t2.html')
		lines=f.readlines()
		rline = lines[286]
		rline2 = lines[297]
		rline3 = lines[296]
		rlink = re.search('[0-9]+', rline)
		rname = re.search('(?<=title\'>)[a-zA-Z0-9_\\s()\\.]+', rline2)
		if rname:
			print 'http://osu.ppy.sh/s/' + rlink.group(0) + '  ' + rname.group(0)
			return
		else:
			rname2 = re.search('(?<=title\'>)[a-zA-Z0-9_\\s()\\.]+', rline3)
			if rname2:
				print 'http://osu.ppy.sh/s/' + rlink.group(0) + '  ' + rname2.group(0)
				return
			else:
				print 'No results found.'
				return
		os.system('rm ~/tempbc/t2.html')
		return
if __name__ == '__main__':
    main(sys.argv[1:])
