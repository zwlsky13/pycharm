#!/usr/bin/env python
# encoding: utf-8

"""
@Version: Python 3.6.2
@Author: zwl
@File: main.py
@Time: 2017/12/21 10:43
"""
def account_information():
    '''
    账户信息
    :return:
    '''
    pass

def account_repayment():
    '''
    还款
    :return:
    '''
    pass

def account_receivables():
    '''
    收款
    :return:
    '''
    pass

def account_transfer():
    '''
    转账
    :return:
    '''
    pass

def account_statement():
    '''
    账单
    :return:
    '''
    pass

def account_logout():
    '''
    用户退出
    :return:
    '''
    pass


def interactive(acc_data):
    '''
    菜单栏
    :param acc_data:
    :return:
    '''
    menu = u'''
    -------ATM-------
    \033[32;1m
    1、账号信息
    2、还款
    3、收款
    4、转账
    5、账单
    6、退出\033[0m'''
    print(menu)

def running():
    '''
    输入账号和密码
    :return:
    '''
    acc_name=input('请输入你的账号：')
    acc_pass=input('请输入密码：')
    print(acc_name,acc_pass)

#interactive(1)

running()











