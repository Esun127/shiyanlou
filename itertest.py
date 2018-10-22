#!/usr/bin/env python3
import sys
testlist = ['Linux', 'Java', 'Python', 'DevOps', 'Go']

it = iter(testlist)

print('Loop Start...')  
while True:
    try:
        course = next(it)
        print(course)
    except Exception as e:
        print("Loop End",e)
        sys.exit(-1)
