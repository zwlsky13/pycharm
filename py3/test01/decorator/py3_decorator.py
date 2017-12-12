#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@Project: py3
@File: py3_decorator.py
@Time: 2017/09/01 11:15
"""
import time

# def time_count(f):
#     def ret():
#         start_time=time.time()
#         f()
#         end_time=time.time()
#         print("spend %s"%(end_time-start_time))
#     return ret
# @time_count   # foo=time_count(foo)
# def foo():
#     time.sleep(2)
#     print('i am foo.')
#
# @time_count   ## bar=time_count(bar)
# def bar():
#     print('start function')
#     time.sleep(5)
#     print('i am bar')
# foo()
# bar()
###########################################################################################
# def time_count1(f):
#     def ret(*x,**y):
#         start_time=time.time()
#         f(*x,**y)
#         end_time=time.time()
#         print("spend %s"%(end_time-start_time))
#     return ret
#
#
#
# @time_count1      # add=time_count(add)
# def add(*a,**b):
#     sums=0
#     for i in a:
#         sums+=i
#     print(sums)
#     time.sleep(2)
# add(1,3,4,100)

###############################################################################################
def logs(flag):
    def time_count2(f):
        def ret(*x,**y):
            start_time=time.time()
            f(*x,**y)
            end_time=time.time()
            print("spend %s"%(end_time-start_time))
            if flag=='true':
                print('this is logs')
        return ret
    return time_count2


@logs('faaaa')      #@time_count2==>add=time_count2(add)
def add(*a,**b):
    sums=0
    for i in a:
        sums+=i
    print(sums)
    time.sleep(2)
add(1,3,4,100)
