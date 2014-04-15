#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from os import path
import logging as Log
Log.basicConfig( level = Log.DEBUG,format = '%(name)s -  %(message)s' )
root_path = path.dirname(path.realpath(__file__))[:-7]
import sqlite3
from common.crypto import crypto


class sql(object):

    """Docstring for sql. """

    def __init__(self):
        """@todo: to be defined1. """
        self.c = crypto()

    def connect(self):
        """@todo: Docstring for connect.
        :returns: @todo

        """
        return sqlite3.connect(root_path+"/data/alice.db")


    def user_exist(self,  **kwargs):
        """@todo: Docstring for chack_user.

        :**kwargs: @todo
        :returns: @todo

        """
        if kwargs.has_key('name'):
            with self.connect() as conn:
	        cur = conn.cursor()
	        cur.execute('select * from users where name="'+kwargs['name']+'";')
	        user = cur.fetchone()
                try:
                    name = user[1]
                    return True
                except:
                    return False
        else:
            return None
    
    def get_key(self,  **kwargs):
        """@todo: Docstring for get_key.

        :name: @todo
        :returns: @todo

        """
        with self.connect() as conn:
	    cur = conn.cursor()
	    cur.execute('select key from users where name="'+kwargs['name']+'";')
	    return cur.fetchone()[0]

    def get_user(self,  **kwargs):
        """@todo: Docstring for get_key.

        :name: @todo
        :returns: @todo

        """
        with self.connect() as conn:
	    cur = conn.cursor()
	    cur.execute('select * from users where name="'+kwargs['name']+'";')
	    return cur.fetchone()


    def register_user(self, **kwargs):
        """@todo: Docstring for register_user.

        :**kwargs: @todo
        :returns: @todo

        """
        if kwargs.has_key('name'):
            if self.user_exist(**kwargs) == False:
                ## Make User 
                name = kwargs['name']
                key = self.c.gen_uniq_key()
                with self.connect() as conn:
	            cur = conn.cursor()
	            cur.execute('insert into users(name,key) values(?, ?);', (name, key))
	            conn.commit()

                rd = {}

                return key
            else:
                return 'user exist'
        else:
            return 'name is required'

    

