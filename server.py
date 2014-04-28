#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
root_path = path.dirname(path.realpath(__file__))
from server.handlers.base import base_commands
from SOAPpy import ThreadingSOAPServer
from M2Crypto import SSL
from M2Crypto import threading    
import logging

logFormatter = logging.Formatter("%(asctime)s %(name)s [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

#fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
#fileHandler.setFormatter(logFormatter)
#rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)



threading.init()
ssl_context = SSL.Context()
ssl_context.load_cert('server/certificates/server.pem')
commands=base_commands()    
server = ThreadingSOAPServer(("localhost",3333), ssl_context = ssl_context)
server.registerObject(commands)
server.serve_forever()


