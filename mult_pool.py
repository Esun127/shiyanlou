#!/usr/bin/env python3

# Pool : you xian ge shu jin cheng
#	   : ke chong yong
#      : ren wu ke neng hui deng dai mou yi jin cheng de xian cai hui yun xing 
from multiprocessing import Pool

def f(i):
	#print(i, end=' ')    			# jie guo: shun xu cuo wei
	print(i, end=' ', flush=True)   # jie guo: shun xu zheng chang



def main():
	pool = Pool(processes = 3)
	for i in range(30):
		# gei jin cheng chi fen pei 30 ge ren wu, da yin chuan ru can shu
		pool.apply(f, (i,))
	pool.close()
	pool.join()

if __name__ == "__main__":
	main()   


