#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import SOAPpy
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tools import job
from time import sleep 
from os import path, listdir, unlink
root_path = path.dirname(path.realpath(__file__))[:-6]
job_path = root_path + 'jobs/'
#print job_path

import logging
logFormatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

#fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
#fileHandler.setFormatter(logFormatter)
#rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

class worker(object):

    """Docstring for worker. """

    def __init__(self):
        """@todo: to be defined1. """
        self.job = job()
        # clear all pids
        for prj in listdir(job_path):
            for files in  listdir(job_path+prj + '/pids/'):
                try:
                    unlink(job_path+prj+'/pids/'+files)
                except:
                    pass 

    def clear_pids(self,  name):
        """@todo: Docstring for clear_pids.

        :name: @todo
        :returns: @todo

        """
        _path = job_path + name + "/"
        if path.exists(_path):        
            try:
                pids = listdir(_path+'pids/')
                for files in pids:
                    unlink(files)
            except:
                pass
        else:
            return 'Error: project not found on this server'
        

    def get_pids_list(self, name):
        """@todo: Docstring for get_pids_list.
        :returns: @todo

        """
        _path = job_path + name + "/"
        if path.exists(_path):        
            try:
                return listdir(_path+'pids/')  
            except:
                return []
        else:
            return 'Error: project not found on this server'
        
    def visit(self,  driver, url):
        """@todo: Docstring for visit.

        :driver: @todo
        :url: @todo
        :returns: @todo

        """
        try:
            driver.get(url)
            logging.info(u"Открыта страница: "+driver.current_url)
        except:
            logging.error(u"Ошибка при открытии страницы")

    def do(self,  name):
        """@todo: Docstring for visit.

        :name: @todo
        :returns: @todo

        """       
        
        ## Get Key
        key = self.job.get_job_key(name)
        ## Get Config
        cfg = self.job.get_config(name)
        server = SOAPpy.SOAPProxy(cfg['server'])
        #resp = server.get_control(name, key)
        while server.get_control(name, key)['active'] == 'True':
            ## Get Job
            job = server.get_job(name, key)
            url, ua, proxy = job['url'], job['ua'], job['proxy'].split(':')
            ## Настройка selenium
            service_args = ['--proxy='+proxy[0]+':'+proxy[1], '--proxy-type='+proxy[2].replace('\n',''), ]
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = (ua)
            driver = webdriver.PhantomJS(executable_path="bin/phantomjs", service_args=service_args, desired_capabilities=dcap) # or add to your PATH
            driver.set_window_size(1920, 1024) # optional
            driver.set_page_load_timeout(15)
            driver.set_script_timeout(15)
            #Store pid
            self.job.store_pid(name, driver.service.process.pid) 
            print self.get_pids_list(name)
            # Do some
            self.visit(driver, url)
            sleep(10)
            try:
                self.job.delete_pid(name, driver.service.process.pid)
                driver.close()
            except:
                pass 

            sleep(10)

if __name__ == '__main__':
    w = worker()
    print w.do('shalenakrasa')

