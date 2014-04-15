#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
import logging as Log
Log.basicConfig( level = Log.DEBUG,format = '%(name)s -  %(message)s' )
root_path = path.dirname(path.realpath(__file__))
from handlers.base import base_commands
from SOAPpy import ThreadingSOAPServer
from M2Crypto import SSL
from M2Crypto import threading    

threading.init()
ssl_context = SSL.Context()
ssl_context.load_cert('certificates/server.pem')
commands=base_commands()    
server = ThreadingSOAPServer(("localhost",3333), ssl_context = ssl_context)
server.registerObject(commands)
server.serve_forever()


