#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from os import urandom
import hashlib

class crypto(object):

    """Docstring for crypto. """

    def __init__(self):
        """@todo: to be defined1. """
    
    def gen_uniq_key(self):
        """@todo: Docstring for gen_uniq_key.
        :returns: @todo

        """
        hash_object = hashlib.sha512(urandom(1024))
        return hash_object.hexdigest()
        
if __name__ == '__main__':
    c = crypto()
    print c.gen_uniq_key()

