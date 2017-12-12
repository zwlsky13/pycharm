#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: logging_module2.py
@time: 2017/12/7 7:13
"""

import logging

logger = logging.getLogger()

# 创建一个handler，用于写入日志文件

fh = logging.FileHandler('test2.log')

# 再创建一个handler，用于输出到控制台

ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)

ch.setFormatter(formatter)

logger.addHandler(fh)  # logger对象可以添加多个fh和ch对象

logger.addHandler(ch)

logger.debug('logger debug message')

logger.info('logger info message')

logger.warning('logger warning message')

logger.error('logger error message')

logger.critical('logger critical message')

