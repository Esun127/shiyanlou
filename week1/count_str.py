#!/usr/bin/env python3

def char_count(string):
	char_list = set(string)
	for char in char_list:
		print(char,str(sorted(string)).count(char))

if __name__ == '__main__':
	s = input("Enter a string: ")
	char_count(s)
