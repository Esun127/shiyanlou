#!//usr/bin/env python3

import sys

less_3 = []
bigeq_3 = []
for arg in sys.argv[1:]:
	if len(arg) <= 3:
		less_3.append(arg)
	else:
		bigeq_3.append(arg)

print(' '.join(less_3))
print(' '.join(bigeq_3))
