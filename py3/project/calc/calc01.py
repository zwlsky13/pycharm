#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: calc01.py
@time: 2017/11/28 23:09
"""

import re

#str1="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#str2="1 - 2 * ( (60-30 +-8 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

# ret=re.search("\([^()]+\)",str2).group()
#
# print(ret)
#
# print(eval(str1))
def format_sting(string):
    string=string.replace("--","+")
    string=string.replace("-+","-")
    string=string.replace("++","+")
    string=string.replace("+-","-")
    string=string.replace("*+","*")
    string=string.replace("/+","/")
    string=string.replace(' ','')
    return string

def mult_div(string):
    #从字符串中获取乘法或者除法式子
    regular='[\-]?\d+\.?\d*([/*]|\*\*)[\-]?\d+\.?\d*'
    while re.findall(regular,string):
        expression = re.search(regular,string).group()
        if expression.count("*")==1:
            x,y=expression.split("*")
            mul_result=str(float(x)*float(y))
            #将表达式替换为计算的结果
            string=string.replace(expression, "+"+mul_result)
            string=format_sting(string)
        elif expression.count("/")==1:
            x, y = expression.split("/")
            mul_result = str(float(x) / float(y))
            # 将表达式替换为计算的结果
            string = string.replace(expression, "+"+mul_result)
            string = format_sting(string)
        elif expression.count("*")==2:
            x, y = expression.split("**")
            mul_result = str(float(x) ** float(y))
            # 将表达式替换为计算的结果
            string = string.replace(expression, "+"+mul_result)
            string = format_sting(string)
    return string
def add_sub(string):
    # 从字符串中获取加法或者减法式子
    # regular = '[\-]?\d+\.?\d*([+-])[\-]?\d+\.?\d*'
    add_regular='[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*'
    sub_regular='[\-]?\d+\.?\d*\-[\-]?\d+\.?\d*'
    #开始加法
    while re.findall(add_regular,string):
        add_list=re.findall(add_regular,string)
        for add_string in add_list:
            x,y=add_string.split("+")
            add_result="+" + str(float(x) + float(y))
            string=string.replace(add_string,str(add_result))
        string=format_sting(string)
    #开始减法
    while re.findall(sub_regular,string):
        sub_list=re.findall(sub_regular,string)
        for sub_string in sub_list:
            number=sub_string.split("-")
            if len(number)==3:
                sub_result = 0
                for v in number:
                    if v:
                        sub_result -= float(v)
            else:
                x,y = number
                sub_result=float(x) - float(y)
            #替换字符串
            string=string.replace(sub_string,"+" + str(sub_result))
            string=format_sting(string)
    return string



source="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#source="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# if check_format(source):
print('真实答案:',eval(source))
source=format_sting(source)
print(source)
while source.count("(") > 0:
    #格式化，去括号
    strs=re.search('\([^()]*\)',source).group()
    #先进行乘除
    strs_replace=mult_div(strs)
    #再进行加减
    strs_replace=add_sub(strs_replace)
    #将括号的字符串替换为结果，结果里包含括号，去掉括号[1:-1]
    source=format_sting(source.replace(strs,strs_replace[1:-1]))
else:
    strs_replace=mult_div(source)
    strs_replace=add_sub(strs_replace)
    source=source.replace(source,strs_replace)
source=source.replace("+",'')
print(source)

