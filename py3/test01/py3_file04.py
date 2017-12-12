#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@Project: py3
@File: py3_file04.py
@Time: 2017/08/02 15:09
"""
# name=input("name:")
# age=input("age:")
# job=input("job:")
# salary=input("salary:")
# if salary.isdigit():
#     salary = int(salary)
# else:
#     exit("must be input digit")


# msg='''
# ------------info of %s---------------
# Name:%s
# Age:%s
# Job:%s
# Salary:%s
# ---------------end-------------------
# '''% (name,name,age,job,salary)
# print(msg)

# x=[1,3,2,8,6,9]
# x.sort(reverse=True)
# print(x)

# a=10
# b=a
# del a
# a=20
# print(id(a))
# print(id(b))

# li=[1,2,3,4,5]
# tu=(6,7,8,9,0)
# dic={'name':'alex','age':18,'job':'it','salary':2222,'is_handsome':True}
# print(dic)
# print(dic['is_handsome'])
# print(id(dic))
#
# print(tuple(li))
#
# print(list(tu))
# dic={1:21,4:12,3:34,5:9}
# print(sorted(dic.items()))
# print(dic)
# for i in dic:
#     print(i,dic[i])
# st='Hello,World,my name is {name},I do {job}'
# # print(st.center(100,'='))
# print(st.format(name='Alex',job='IT'))
a=['a','b','c','d']
print(''.join('a[0]','a[1]','a[2]','a[3]'))
