#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import SOAPpy

server = SOAPpy.SOAPProxy("https://127.0.0.1:3333/")

resp = server.get_control('shalenakrasa')
print resp
resp = server.get_config('shalenakrasa')
print resp
resp = server.get_job('shalenakrasa')
print resp
resp = server.refresh_proxy()
print resp







