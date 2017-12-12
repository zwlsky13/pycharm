#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@File: py3_file03.py
@Time: 2017/08/01 15:03
"""

class D(object):
    def bar(self):
        print('D.bar')

class C(D):
    def bar(self):
        print('C.bar')

class B(D):
    def bar1(self):
        print('B.bar')

class A(B,C):
    def bar1(self):
        print('A.bar')

a=A()
a.bar()
