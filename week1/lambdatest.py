#!/usr/bin/env python3

list1 = [('Shi',100), ('Yan',75), ('Lou',200), ('Plus',80)]

get_value = lambda t: t[1]
sortedlist = sorted(list1, key=get_value)
print(sortedlist)
