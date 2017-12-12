#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: re.py
@time: 2017/11/2 6:34
"""
import re

# ret=re.findall('[wea]','awera*')
# print(ret)
# ret=re.findall('abc[3,4]','werabc4,wew')
# print(ret)
###################################################################
# ret=re.findall('\wcde','abqcdef')
# ret1=re.findall('\Wcde','ab*cdef')
# ret2=re.findall(r'e\b','abcd*e*f*h')
# print(ret)
# print(ret1)
# print(ret2)
# ret3=re.search('ad','dsadfdg').group()
# print(ret3)
# '''
# 显示输出
# ['qcde']
# ['*cde']
# ['e']
# ad
# '''
##################################################################
# ret=re.search('(?P<id>\d{3})/(?P<name>\w{3})','weew34ttt123/ooo')
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))
# '''
# 显示输出
# 123/ooo
# 123
# ooo
# '''

# ret=re.search('\([^()]+\)','(2+5)*8/(10-8)')
# print(ret)


# a="1++2--4"
# print(a.replace('++','**'))


###########################################
#1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )

str="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
str1="(1+=2)"
# while str1.count("(")>0:
#     ret=re.search("\([^()]*\)",str1).group()
#     print(ret)

# print(str1[1:-1])
#
# a="2"
# b="4"
# c=float(a)**float(b)
# print(c)
#
# regular='[\-]?\d+\.?\d*(?:[/*]|\*\*)[\-]?\d+\.?\d*'
# str="12*3+13*2"
# print(re.search(regular,str).group())
# print(re.findall(regular,str))
a="abcde"
b="cd"
c="HGTK"
print(a.replace(b,"+"+c))

add_regular='[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*'
tring="13+23,12+2"
ret=re.findall(add_regular,tring)
print(ret)
c="1+2"
a=['1+2']
b="vf"

print(c.replace(a,b))