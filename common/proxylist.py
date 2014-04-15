#!/usr/bin/python
# -*- coding: latin1 -*-
from grab import Grab, GrabError
from os import path, unlink
import subprocess
import logging
#logging.disable(logging.ERROR)

root_path = path.dirname(path.realpath(__file__))[:-6]
tmp = root_path+"tmp/"

class proxy(object):

    """Docstring for proxy. """

    def __init__(self):
        """@todo: to be defined1. """
    
    def make_proxy_lists(self):
        """@todo: Docstring for make_alive.
        :returns: @todo

        """
        self.get_proxy_premium()
        alive_list =  self.get_valid_proxy(root_path+'/data/lists/proxy.list')

        with open(root_path+'/data/lists/alive.list', 'w') as f:
            for i in alive_list:
                print i
                f.write(i+'\n')

        

    def get_valid_proxy(self, proxy_list): #format of items e.g. '128.2.198.188:3124'
        with open(proxy_list,'r') as f:
            proxy_list=f.readlines()
        g = Grab()
        for proxy in proxy_list:
            g.setup(proxy=proxy, proxy_type='http', connect_timeout=1, timeout=5)
            try:
                g.go('google.com', timeout=10)
            except GrabError:
                pass 
            else:
                try:
                    if g.xpath_list('//title')[0].text == u'Google':
                        print g.xpath_list('//title')[0].text
                        yield proxy.replace('\n','')+":http"
                except:
                    print "Bad proxy" 
    
    def get_proxy_premium(self,  code='989570157'):
        """@todo: Docstring for get_proxy_premium.

        :code: @todo
        :returns: @todo

        """
        g=Grab()
        g.go('http://hideme.ru/api/proxylist.php?country=ALAMAUBEBGCACZEEFRGEDEILITKZLVMDNLANPLRORUCHTRUAGB&type=h&anon=1234&out=plain&code='+code)
        jlist = g.response.body.split()
        print jlist
        with open(root_path+'/data/lists/alive.list','w') as f: 
            for proxy in jlist:
                f.write(proxy+":http\n")


if __name__ == '__main__':
    p=proxy()
#    p.make_proxy_lists()
    p.get_proxy_premium()
