#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import SOAPpy

server = SOAPpy.SOAPProxy("https://127.0.0.1:3333/")

resp = server.get_control('shalenakrasa','0b468792419fd869f2e484a12f4073f6592e2a556664ac6d2306b5f8da1f172281405afd478896da1474ce4d5e3e52f3e791761e3d9843aa438939bc1a80df2a')
print resp
resp = server.get_config('shalenakrasa','0b468792419fd869f2e484a12f4073f6592e2a556664ac6d2306b5f8da1f172281405afd478896da1474ce4d5e3e52f3e791761e3d9843aa438939bc1a80df2a')
print resp
resp = server.get_job('shalenakrasa','0b468792419fd869f2e484a12f4073f6592e2a556664ac6d2306b5f8da1f172281405afd478896da1474ce4d5e3e52f3e791761e3d9843aa438939bc1a80df2a')
print resp
#resp = server.refresh_proxy()
#print resp





