#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: py3_time_module.py
@time: 2017/9/13 22:13
"""
import time

# time.sleep(3)
# print(time.clock())  #cpu执行时间
# print(time.gmtime())
# print(time.clock())
# print(time.localtime())
#
# print(help(time.strftime))
# print(time.strftime('%Y--%m--%d %H:%M:%S %z %a %A %b %B %c'))

# struct_time=time.localtime()#本地时间
# print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time))
# #2017-09-13 22:54:06
# a=time.strptime('2017-09-13 22:52:12','%Y-%m-%d %H:%M:%S')
# # print(a)
# #time.struct_time(tm_year=2017, tm_mon=9, tm_mday=13, tm_hour=22, tm_min=52, tm_sec=12, tm_wday=2, tm_yday=256, tm_isdst=-1)
# print(a.tm_yday)
# print(a.tm_mday)
# print(a.tm_wday)
# print(time.ctime(3600))#括号里的填写时间戳，转化为时间格式输出
# print(time.mktime(time.localtime()))#转化为时间戳
import datetime
print(datetime.datetime.now())
print(time.time())


