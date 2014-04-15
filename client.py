#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import SOAPpy

server = SOAPpy.SOAPProxy("https://127.0.0.1:3333/")
d = {}
d['project'] = 'shalenakrasa'
resp = server.get_control('shalenakrasa')
print resp





