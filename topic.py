#!/usr/bin/env python

import sys

if not sys.argv[1].startswith("!"):
	print "/topic", " ".join(sys.argv[1:])


