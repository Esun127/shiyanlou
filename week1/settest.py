#!/usr/bin/env python3
import sys
uniq=set()

for arg in sys.argv[1:]:
	uniq.add(arg)

print(' '.join(uniq))
