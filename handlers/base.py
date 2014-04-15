#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
import logging 
from common.database import sql
from common.jobs import jobs
from random import choice, randint
from common.proxylist  import proxy
root_path = path.dirname(path.realpath(__file__))[:-9]

logger = logging.getLogger('base')
hdlr = logging.FileHandler(root_path+'/alice.log')
formatter = logging.Formatter(u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)


class base_commands(object):

    """Docstring for base_commands. """

    def __init__(self):
        """@todo: to be defined1. """
        self.db = sql()
        self.job = jobs()
        self.proxy = proxy()

    def ping(self):
        """@todo: Docstring for ping.
        :returns: @todo

        """
        logger.info('ping - pong')
        return 'pong'

    def get_config(self,  name):
        """@todo: Docstring for get_config.

        :name: @todo
        :returns: @todo

        """
        return self.job.get_config(name)

    def get_control(self, name):
        """@todo: Docstring for get_control.

        :name: @todo
        :returns: @todo

        """
        return self.job.get_control(name)

    def refresh_proxy(self):
        """@todo: Docstring for refresh_proxy.
        :returns: @todo

        """
        try:
            self.proxy.get_proxy_premium()
            return "Proxy list are fresh"
        except:
            return 'Error refreshing proxy list'

    def get_job(self, name):
        """@todo: Docstring for get_job.

        :**kwargs: @todo
        :returns: @todo

        """
        resp = {}
        try:
            url = choice(self.job.get_job_link(name))
        except:
            url = 'None'
        resp['proxy']  = self.job.get_random_proxy()
        resp['url'] = url
        resp['ua'] = self.job.get_random_ua()
        return resp 







