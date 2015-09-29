#!/usr/bin/env python
# !bloodcat v0.2
# because dan's implementation sucks big dick

import sys
import json
import urllib

args = sys.argv[1:]
TEMPLATE_URL = "http://bloodcat.com/osu/?mod=json&q={}"

if len(args)>0:
	query = "+".join(args)
	queryUrl = TEMPLATE_URL.format(query)

	try:
		response = urllib.urlopen(queryUrl)
		data = json.loads("".join(response.readlines()))
	except Exception:
		print "rip server, try again later"
		sys.exit()

	# data exists
	# we now need to get first element (because why not)
	beatmapList = data[u"results"]
	try:
		beatmap = beatmapList[1]
	except Exception:
		# hax
		print "No results found :("
		sys.exit()
	# now print out
	templateOutput = "http://bloodcat.com/osu/s/{id} {artist} - {title} (mapped by {creator})"
	print templateOutput.format(**beatmap)
else:
	print "Usage: !bc [query]"
	print "Outputs the first search result."

