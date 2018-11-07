#!/usr/bin/env python3

filename = input("Enter the filename:")
with open(filename, 'r') as f:
    content = f.readlines()
    for linenum, line in enumerate(content):
        print("{}".format(line))
    print('lines:{}'.format(linenum+1))
