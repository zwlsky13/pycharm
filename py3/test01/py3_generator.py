#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: py3_generator.py
@time: 2017/9/10 21:55
"""
# s=(x*2 for x in range(100000000000))
# print(s)    #generator object
# print(next(s))   #等价于s.__next__() 在py2里面
# print(next(s))
# def foo():
#     print('ok')
#     yield 1
#     print('ok2')
#     yield 2
#     print('ok3')
#     yield 3
#
# g=foo()
# for i in g:
#     print(i)

# def foo():
#     print('ok1')
#     count=yield 1
#     print(count)
#     yield 2
#
# b=foo()
# a=b.send(None)#next(b) 第一次send前如果没有next，只能传一个send（None）
# c=b.send('abc')
# print(a)
# print(c)


import time


def consumer(name):
    print("%s 准备吃包子啦!" % name)

    while True:
        baozi = yield

        print("包子[%s]来了,被[%s]吃了!" % (baozi, name))


def producer():
    c = consumer('A')       #c是生成器对象，还没执行

    c2 = consumer('B')

    c.__next__()            #执行生产器对象

    c2.__next__()

    print("老子开始准备做包子啦，只做十次！")

    for i in range(10):
        time.sleep(1)

        print("做了2个包子!")
        print("第%s次包子"%(i+1))
        c.send('a')

        c2.send('b')


producer()





