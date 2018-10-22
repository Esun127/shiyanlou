#!/usr/bin/env python3

from multiprocessing import Process, Queue
import queue as qqq

queue = Queue(1)

def putin(q):
	l = ['Hello', 'shiyanlou']
	for i in l:
		q.put(i)
		print('Send Data:{}'.format(i))

def getout(q):
#	while True:
#	#while not q.empty():
#		try:
#			data = q.get(timeout=0.1)
#			print('Receive Data:{}'.format(data))
#		except qqq.Empty:
#			return 
	while True:
		data = q.get()
		print('Receive Data:{}'.format(data))
		if q.empty():
			return

		


def main():
	Process(target=putin, args=(queue,)).start()
	Process(target=getout, args=(queue,)).start()


if __name__ == '__main__':
	main()
