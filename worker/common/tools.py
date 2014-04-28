#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
from os import path, unlink
root_path = path.dirname(path.realpath(__file__))[:-6]
job_path = root_path + 'jobs/'

class job(object):

    """Docstring for job. """

    def __init__(self):
        """@todo: to be defined1. """

    def store_pid(self, name, pid):
        """@todo: Docstring for get_job_key.

        :name: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"
        if path.exists(_path):        
            try:
                with open(_path+'pids/'+str(pid), 'w') as f:
                    f.write('')
            except:
                print "Error write a pid file"
        else:
            return 'Error: project not found on this server'
    
    def delete_pid(self,  name, pid):
        """@todo: Docstring for delete_pid.

        :name: @todo
        :pid: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"
        if path.exists(_path):        
            try:
                unlink(_path+'pids/'+str(pid))    
            except:
                pass 
        else:
            return 'Error: project not found on this server'
        


    def get_job_key(self, name):
        """@todo: Docstring for get_job_key.

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

    def get_config(self,  name):
        """@todo: Docstring for get_job.

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
