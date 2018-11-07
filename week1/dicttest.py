#!/usr/bin/env python3
import sys

output_dict = {}

def handle_data(arg):
	k, v = arg.split(':')
	output_dict[k] = v

if __name__ == '__main__':

	for arg in sys.argv[1:]:
		handle_data(arg)


	for k in output_dict:
		print('ID:{} Name:{}'.format(k,output_dict.get(k)))


