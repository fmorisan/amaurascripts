#!/usr/bin/env python
import urllib
import json
import sys

try:
	args = sys.argv[1:]
	assert args[0] != "-h"
	raw_json = urllib.urlopen("https://osu.ppy.sh/api/get_user?k=46ee8da7748ba83f6836563aa90f1d19626a9052&u="+args[0]+"&type=string").read()
	response = json.loads(raw_json)[0]
	try:
		print "Stats for {}:".format(response["username"]),
		print "Rank: #{}, pp: {}, acc: {:.2f}%".format(response["pp_rank"], response["pp_raw"], float(response["accuracy"]))
	except Exception:
		pass
except Exception, e:
	if not raw_json:
		print "Error: something happened with the API"
	else:
		print "Usage: !userstats [<username>|-h]"
		print "'-h' stands for help because you might want to break the command while searching for some guy called 'help'"
