#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import SOAPpy
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
                ## 
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
        

    def register(self, login, password):
        """@todo: Docstring for register.

        :name: @todo
        :returns: @todo

        """
        ## Get config
        cfg = SafeConfigParser()
        cfg.read(root_path+"worker.conf")
        cfg_dict = dict(cfg._sections['global']) 
        ## Packet 
        payload = {}
        payload['login'] = login
        payload['password'] = password
        payload['uid'] = cfg_dict['uid']
        payload['inbound_ip'] = cfg_dict['inbound_ip']
        ## Request
        try:
            server = SOAPpy.SOAPProxy(cfg_dict['server'])
            resp = server.register(payload)
            print resp
        except:
            print 'Error connect to server: '+ cfg_dict['server']




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

if __name__ == '__main__':
    a = job()
    a.register('neuro', '1978cyberD')
