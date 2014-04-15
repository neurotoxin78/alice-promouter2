#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from common.database import sql
from common.crypto import *

s=sql()
d={}
d['name'] = 'neuro'
print s.get_user(**d)


