#!/usr/bin/env python
# encoding: utf-8

"""
@Version: Python 3.6.2
@Author: zwl
@File: account_sample.py
@Time: 2017/12/26 11:20
"""
import os
import sys
import json
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(BASE_DIR)

account_info={
    'id':'100001',
    'name':'sky',
    'balance':'100000',
    'creadit':'200000',
    'enroll_date':'2017-12-22',
    'expire_date':'2018-01-01',
    'status':0    #0:正常，1：锁定，2：失效
}
account_file=os.path.join(BASE_DIR,'db','accounts',account_info['name']+'.json')
# print(account_file)
with open(account_file,'w+') as f:
    w=json.dumps(account_info)
    f.write(w)





