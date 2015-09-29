#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import os
import sys
import time

if os.environ["SKYPE_USERNAME"] in ('euphoricradioactivity', 'fmorisan'):
	print "Stop spamming! Bot will sleep for 1 minute."
	time.sleep(60)
else:
	print "You're not authorized to use this command."
sys.exit(1)
