#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: py3_random.py
@time: 2017/9/13 23:28
"""
import random
# print(random.random())#随机数，不超过1
# print(random.randint(1,9))#包括8，随机数,指定范围
# print(random.choice('hello'))
# print(random.choice([1,3,4,'qweq']))#只选择一个值
# print(random.sample([1,3,4,'qweq',['a','bfd','aw1']],2))#随机选数，选2个，可以控制值的个数
# print(random.randrange(1,3))#随机选，不包含3
def v_code():
    # list=[]
    code=''
    for i in range(5):
    #     if i == random.randint(0,7):
    #         add=random.randrange(10)
    #     else:
    #         add=chr(random.randint(65,90))
    #     code+=str(add)
        add=random.choice([random.randint(0,9),chr(random.randint(65,90))])
        code += str(add)
    print(code)

v_code()
# print(help(random.choices))
# print(random.choices(['q','wwrrtt','e','q'],weights=None,cum_weights=['w','q'],k=1))