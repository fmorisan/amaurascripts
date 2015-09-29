#!/usr/bin/env python

import os, sys
template = "i was fucking {}. -{}"
print template.format(" ".join(sys.argv[1:]), os.environ["SKYPE_FULLNAME"])
