#!/usr/bin/env python3
def connect(ipaddress, ports):
	print('IP:',ipaddress)
	print('PORTS:',ports)
	ipaddress = '10.10.10.1'
	ports.append(8080)

if __name__ == '__main__':
	ipaddress = '192.168.1.1'
	ports = [22,23,24]
	print('Before connect:')
	print('IP:',ipaddress)
	print('POPTS:',ports)
	print('In connect:')
	connect(ipaddress, ports)
	print('After connect:')
	print('IP:',ipaddress)
	print('POPTS:',ports)
