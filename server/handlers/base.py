#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path 
from server.common.database import sql
from server.common.jobs import jobs
from random import choice, randint
from server.common.proxylist  import proxy
root_path = path.dirname(path.realpath(__file__))[:-9]

import logging
logFormatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

#fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
#fileHandler.setFormatter(logFormatter)
#rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


class base_commands(object):

    """Docstring for base_commands. """

    def __init__(self):
        """@todo: to be defined1. """
        self.db = sql()
        self.job = jobs()
        self.proxy = proxy()

    def check_user(self,  data):
        """@todo: Docstring for check_user.

        :data: @todo
        :returns: @todo

        """
        try:
            login = data['login']
            passw = data['password']
            user_data = self.db.get_user(login)
            if user_data != None:
                ## Check password
                if passw == user_data[2]:
                    return True
                else:
                    return 'wrong password'
        except:
            return 'invalid request struct'
        
    def register(self,  data):
        """@todo: Docstring for register.

        :data: @todo
        :returns: @todo


        """
        auth = self.check_user(data)
        if auth == True:
            return self.db.register_client(data)
        else:
            return auth



    def ping(self):
        """@todo: Docstring for ping.
        :returns: @todo

        """
        logging.info('ping - pong')
        return 'pong'

    def get_config(self,  name, key):
        """@todo: Docstring for get_config.

        :name: @todo
        :returns: @todo

        """
        if self.job.get_job_key(name) == key:
            return self.job.get_config(name)
        else:
            return 'key error'

    def get_control(self, name, key):
        """@todo: Docstring for get_control.

        :name: @todo
        :returns: @todo

        """
        if self.job.get_job_key(name) == key:
            return self.job.get_control(name)
        else:
            return 'key error'

    def refresh_proxy(self):
        """@todo: Docstring for refresh_proxy.
        :returns: @todo

        """
        try:
            self.proxy.get_proxy_premium()
            return "Proxy list are fresh"
        except:
            return 'Error refreshing proxy list'

    def get_job(self, name, key):
        """@todo: Docstring for get_job.

        :**kwargs: @todo
        :returns: @todo

        """
        if self.job.get_job_key(name) == key:        
            resp = {}
            try:
                url = choice(self.job.get_job_link(name))
            except:
                url = 'None'
            resp['proxy']  = self.job.get_random_proxy()
            resp['url'] = url
            resp['ua'] = self.job.get_random_ua()
            return resp 
        else:
            return "key error"






