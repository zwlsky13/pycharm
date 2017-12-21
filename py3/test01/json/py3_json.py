#!/usr/bin/env python
# encoding: utf-8

"""
@Version: Python 3.6.2
@Author: zwl
@File: py3_json.py
@Time: 2017/12/13 14:43
"""

import json
import pickle
# dic={'name':'Alex','age':38,'sex':'male'}
# print(type(dic))
# j=json.dumps(dic)
# print(type(j))
# f=open('json.txt','w')
# f.write(j)
# # f.write('\n')
# f.close()

# with open('json.txt','a+') as f:
#     dic={'name':'test','age':40,'sex':'male'}
#     k=json.dumps(dic)
#     f.write(k)

with open('json.txt') as f:
    data=f.readline()
    print(type(data))
    # print(str(data))
    # a={}

    a=json.dumps(data)
    b=json.loads(data)
    print(type(b))
    print(b['name'])




# dic='{"name":"test","age":90}'
# print(type(json.loads(dic)))

# dic={'name':'test','age':90}
# with open('pickle.txt','wb') as f :
#     t=pickle.dumps(dic)
#     f.write(t)
#
# with open('pickle.txt','rb') as f:
#     data=pickle.load(f)
#     print(data)










