#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@Project: py3
@File: py3_sys.py
@Time: 2017/10/26 17:32
"""

import sys
import os
real_file=sys.argv
print(real_file)
real_path=os.getcwd()
pwd=os.path.split(os.getcwd())
file_name=os.path.split(real_file[0])
# print(pwd)
# print(file_name)
print(file_name)
