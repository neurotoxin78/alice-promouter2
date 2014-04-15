#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from os import path
root_path = path.dirname(path.realpath(__file__))[:-6]
job_path = root_path + 'jobs/'

class jobs(object):

    """Docstring for jobs. """

    def __init__(self):
        """@todo: to be defined1. """
        self.cfg = SafeConfigParser()

    def get_control(self, name):
        """@todo: Docstring for get_control.

        :name: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"
        self.cfg.read(_path+"control")
        cfg_dict = dict(self.cfg._sections['global']) 
        return cfg_dict
        

    def get_config(self,  name):
        """@todo: Docstring for get_config.

        :name: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"
        self.cfg.read(_path+"config")
        cfg_dict = dict(self.cfg._sections['global']) 
        return cfg_dict

    def get_job_link(self,  name):
        """@todo: Docstring for get_job_data.

        :name: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"

        try:
            with open(_path+'internal_urls', 'r') as f:
                urls = f.read().split()
        except:
            print "Error"

        return urls 

