#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: list_create.py
@time: 2017/9/5 7:54
"""
def f(n):
    return n**3


a=[ f(i) for i in range(10)]

print(a)