#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from os import path
from random import choice 
root_path = path.dirname(path.realpath(__file__))[:-6]
job_path = root_path + 'jobs/'

class jobs(object):

    """Docstring for jobs. """

    def __init__(self):
        """@todo: to be defined1. """
        

    def get_control(self, name):
        """@todo: Docstring for get_control.

        :name: @todo
        :returns: @todo

        """
        
        _path = job_path + name + "/"
        if path.exists(_path):
            cfg = SafeConfigParser()
            cfg.read(_path+"control")
            cfg_dict = dict(cfg._sections['global']) 
        else:
            cfg_dict = 'Error: project not found'
        return cfg_dict 
        

    def get_config(self,  name):
        """@todo: Docstring for get_config.

        :name: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"
        if path.exists(_path):
            cfg = SafeConfigParser()
            cfg.read(_path+"config")
            cfg_dict = dict(cfg._sections['global']) 
        else:
            cfg_dict = 'Error: project not found'
        return cfg_dict 

    def get_random_proxy(self):
        """@todo: Docstring for get_random_proxy.
        :returns: @todo

        """
        with open(root_path+"data/lists/proxies.list","r") as f:
            alive_list = f.readlines()
        
        return choice(alive_list)[:-1]

    def get_random_ua(self):
        """@todo: Docstring for get_random_ua.
        :returns: @todo

        """
        with open(root_path+"/data/uas/uas.txt", "r") as f:
            ua_list = f.readlines()
        return choice(ua_list)[:-1]


    def get_job_link(self,  name):
        """@todo: Docstring for get_job_data.

        :name: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"
        if path.exists(_path):        
            try:
                with open(_path+'internal_urls', 'r') as f:
                    urls = f.read().split()
            except:
                print "Error opening a url file"
        else:
            urls = 'Error: project not found on this server'
        return urls 

    def get_job_key(self,  name):
        """@todo: Docstring for get_job_data.

        :name: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"
        if path.exists(_path):        
            try:
                with open(_path+'key', 'r') as f:
                    key = f.read()
            except:
                print "Error opening a key file"
        else:
            key = 'Error: project not found on this server'
        return key 

