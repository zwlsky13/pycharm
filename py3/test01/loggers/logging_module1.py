#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: logging.py
@time: 2017/12/6 7:32
"""


import logging

logging.basicConfig(level=logging.DEBUG,

                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',

                    datefmt='%a, %d %b %Y %H:%M:%S',

                    filename='test.log',

                    filemode='w')

logging.debug('debug message')

logging.info('info message')

logging.warning('warning message')

logging.error('error message')

logging.critical('critical message')
