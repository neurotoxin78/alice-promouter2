#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from os import path
import logging as Log
Log.basicConfig( level = Log.DEBUG,format = '%(name)s -  %(message)s' )
root_path = path.dirname(path.realpath(__file__))[:-7]
import sqlite3
from crypto import crypto


class sql(object):

    """Docstring for sql. """

    def __init__(self):
        """@todo: to be defined1. """
        self.c = crypto()

    def connect(self, db):
        """@todo: Docstring for connect.
        :returns: @todo

        """
        return sqlite3.connect(root_path+"/data/"+db)


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

    def get_user(self,  login):
        """@todo: Docstring for get_key.

        :name: @todo
        :returns: @todo

        """
        with self.connect('users.db') as conn:
	    cur = conn.cursor()
	    cur.execute('select * from users where login="'+login+'";')
	    return cur.fetchone()

    def client_exist(self, key):
        """@todo: Docstring for client_exist.

        :data: @todo
        :returns: @todo

        """
        with self.connect('client.db') as conn:
	    cur = conn.cursor()
	    cur.execute('select * from clients where key="'+key+'";')
	    return cur.fetchall()
        

    def register_client(self, data):
        """@todo: Docstring for register_user.

        :**kwargs: @todo
        :returns: @todo

        """
        key = data['uid']
        address = 'https://'+data['inbound_ip']+':3334/'
        if not self.client_exist(key):
            with self.connect('client.db') as conn:
                cur = conn.cursor()
        	cur.execute('insert into clients(key,address) values(?, ?);', (key, address))
        	conn.commit()
                return 'Client rigistered successfully'
        else:
            return 'Client exist'
    
if __name__ == '__main__':
    db = sql()
    ar = {}
    ar['name'] = 'neuro'
    print db.get_user('neuro')

