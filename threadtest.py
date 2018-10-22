#!/usr/bin/env python3

import threading

def hello(name):
	# get_ident()  -->  huo qu dang qian xian cheng id
	print('child thread:{}'.format(threading.get_ident()))
	print("Hello " + name)


def main():
	# chu shi hua yi ge xian cheng , can shu chuan di he shi yong jin cheng yi yang
	t = threading.Thread(target=hello, args=('shiyanlou',))
	t.start()
	t.join()
	print('main thread:{}'.format(threading.get_ident()))


if __name__ == '__main__':
	main()
