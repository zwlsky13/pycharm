#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: py3_iterator.py
@time: 2017/9/12 23:10
"""
l=[1,2,3,5]
d=iter(l)   #l._next_()
print(d)
for i in d:
    print(i)        #不断执行print(next(d))



# for 循环内部三件事
#     1 调用可迭代对象的iter方法，返回一个迭代器对象
#     2 不断调用迭代器对象的netx方法
#     3 处理StopIteration








