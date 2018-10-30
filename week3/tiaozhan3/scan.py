#!/usr/bin/env python3

import getopt
import sys
import socket

class Args:
    args = sys.argv[1:]

    def __init__(self, opt_names):
        self.lp = []
        for i in opt_names:
            print('required option: --{} <value>'.format(i))
            i = i + '='
            self.lp.append(i)
        self.options = self._get_options()

    
    def _get_options(self, _sp=None):
        try:
            opts, args = getopt.getopt(self.args, _sp, self.lp)            
        except getopt.GetoptError as e:
            print('Parameter Error',e)
            sys.exit(-1)

        if args:
            print('Parameter Error')
            sys.exit(-2)
        return dict(opts)

    def getvalue_by_optname(self, name):
        name = '--' + name 
        if  name in self.options:
            if name == '--port':
                values = self.options.get(name, None).split('-')
                try:
                    if len(values) == 1:
                        t = int(values[0])
                    elif len(values) == 2:
                        t = range(int(values[0]), int(values[1])+1)
#                        print(t)

                    return t
                except ValueError as e:
                    print('Parameter Error',e)
                    sys.exit(-3)
                



            return self.options.get(name, None)


class Nmap:
    def __init__(self):
        self.cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.cs.settimeout(0.1)


    def close(self):
        return self.cs.close()

    def test(self, host, port):
        try:
            self.cs.connect((host,port))
        except socket.error as e:
            # print(e)
            print('{}: closed'.format(port))
        else:
            print('{}: open'.format(port))
        finally:
            self.close()


if __name__ == '__main__':
    args = Args(['host', 'port'])
    host = args.getvalue_by_optname('host')
    ports = args.getvalue_by_optname('port')
    
    nmap = Nmap()
    if isinstance(ports, int):
        nmap.test(host, ports)
    elif isinstance(ports, range):
        for i in ports:
            nmap.test(host, i)





