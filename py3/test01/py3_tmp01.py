#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@Project: py3
@File: py3_tmp01.py
@Time: 2017/08/29 11:03
"""

# count=10
# def out():
#     global count
#     print(id(count))
#     count=5
#     print(id(count))
# print(id(count))
# out()
# a=set(('a','b','c','d'))
# b=set(('a','g','f','b'))
#
# c=set([1,2,3,4])
# d=set([1,2,3,4,5])
#
# print(a|b)
# print(a&b)
# print(a-b)
# print(a^b)
# print(c<=d)

# def f(n):
#     return n*n
# def foo(a,b,f):
#     return f(a)+f(b)
# print(foo(2,4,f))
# def foo1():
#     def inner():
#         return 8
#     return inner()
# ret=foo1
# print(ret())

# def Factorial(a):
#     s=1
#     for i in range(1,a+1):
#         s=i*s
#     return s
# print(Factorial(5))

# def fat(n):
#     if n==1:
#         return 1
#
#     return n*fat(n-1)
#
# print(fat(7))
#0 1 1 2 3 5 8 13 21 34 55
#斐波拉
# def fibo(n):
#     first=0
#     second=1
#     if n==1:
#         return 0
#     for i in range(3,n):
#         ret=first+second
#         first=second
#         second=ret
#     return first+second
# print(fibo(1))
# def factorial_new(n):
#     if n == 3:
#         return 3
#     return n * factorial_new(n - 1)#f(5)=5*f(4)*f(3)=5*4*f(3)*f(3)
#
#
# print(factorial_new(5))

##filter
# str = ['a', 'b', 'c', 'd']
# str2=(1,2,3,4,5)
#
# def fun1(s):
#     if s != 'a':
#         return s
# def fun2(n):
#     return n*n
#
# ret = map(fun2, str2)
#
# print(list(ret))  # ret是一个迭代器对象

# def foo():
#     print('i am the foo')
#     bar()
# def bar():
#     print('i am the bar')
# foo()
import sys
import os
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

