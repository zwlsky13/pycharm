#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@Project: py3
@File: login.py
@Time: 2017/09/05 10:28
"""
import getpass
import time

def auto_login():
    def logins(f):
        def login():
            f_name, f_passwd = 'zwl', '123'
            global flag
            if flag=='False':
                name = input('请输入用户名：')
                passwd = getpass.getpass('请输入密码：')
                if name==f_name and passwd==f_passwd:
                    print('login is success..')
                    flag = 'True'
                    f()
                else:
                    print('username or password is error,login fail..')
            elif flag=='True':
                f()
        return login
    return logins
def print_error():
    print('输入错误，重新输入。')

@auto_login()  #==>jinrong=auto_login(jinrong)
def jinrong():
    print('这是金融板块。。')

@auto_login()
def chaoshi():
    print('这是超市板块。。')
@auto_login()
def shangcheng():
    print('这是商城板块。。')

mode_dict={1:'jinrong',2:'chaoshi',3:'shangcheng'}
flag = 'False'
while True:
    #print('请输入你要查看的板块：')

    print(mode_dict)
    choise=input('请输入你要查看的板块，退出q：')
    if choise.isdigit():
        if int(choise) in mode_dict:
            choise=int(choise)
            eval(mode_dict[choise])()#==>jinrong()
        else:
            print_error()
    elif choise=='q':
        print('欢迎下次访问。。')
        break
    else:
        print_error()
print(time.clock())