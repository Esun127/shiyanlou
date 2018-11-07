#!/usr/bin/env python3
import sys

ndict = {}
for arg in sys.argv[1:]:
	k, v = arg.split(':')
	ndict[k] = v

for k, v in ndict.items():
	print('ID:{} Name:{}'.format(k,v))
