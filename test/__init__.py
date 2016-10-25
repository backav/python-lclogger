#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bac'

from py_lclogger import logger

logger.log("http://xxxx.xx/log",
           "xxx.47"
           ,"bactestpython/0.2","test py_lclogger",{"X-Error-Code":500})

while True:
    pass
