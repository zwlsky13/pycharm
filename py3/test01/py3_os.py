#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@Project: py3
@File: py3_os.py
@Time: 2017/10/26 15:52
"""
import os

pwd=os.path.join(os.getcwd(),'py3_tmp01.py')
print(pwd)

# os.chdir('/tmp')
print(os.listdir('/tmp'))#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove('/tmp/test.txt')
#print(os.listdir(pwd))
info=os.stat('py3_file04.py')
print(info.st_size)
#os.system('rm -rf /tmp/a')
os .system('date -d @1509028296')
print(os.path.getatime('/datadisk'))
print(os.name)
print(os.path.dirname(pwd))#表示上一个路径 example:/datadisk/python/py3/test01
print(os.path.abspath(pwd))#表示全路径 example:/datadisk/python/py3/test01/py3_tmp01.py
print(os.path.split(pwd))
print(os.linesep)
print(os.pathsep) #输出用于分割文件路径的字符串



