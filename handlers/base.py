#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
import logging 
from common.database import sql
from common.jobs import jobs
from random import choice, randint

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

    def get_job(self,  **kwargs):
        """@todo: Docstring for get_job.

        :**kwargs: @todo
        :returns: @todo

        """
        if kwargs.has_key('project'):
            project = kwargs['project']
            url = choice(self.job.get_job_link(project))
        else:
            project = None
            url = None
        return url





