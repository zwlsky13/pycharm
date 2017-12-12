#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@Project: py3
@File: py3_file_operation01.py
@Time: 2017/08/17 12:20
"""
# f=open('test.txt','a+',encoding='utf8')


# f.write("\ntest\n")
# print(f.readlines())
# for i in f.readlines():
#     print(i.strip())

# a=f.readlines()
#
# a[2]='***'.join([a[2],'ewqeqwrdsa'])
# print(a)
# number=0
# for i in f:
#     number=number+1
#     if number == 2:
#         i = ''.join([i.strip(),'dasdqw'])
#     print(i.strip())
# print(f.tell())
# print(f.read(2))
# print(f.tell())

# f.seek(3)
# print(f.read(4))
# print(f.tell())
# f.seek(0)
# print(f.readline())
# f.write('test')
# print(f.readable())
# # f.truncate(3)
# f.close()

# f_read=open('test.txt','r',encoding='utf8')
# f_write=open('test1.txt','w',encoding='utf8')
# num=0
# for i in f_read:
#     num+=1
#     if num==2:
#         i='++++++++'.join([i.strip(),'ghjk\n'])
#         # f_write.write(i)
#     f_write.write(i)

#同时管理多个文件对象
# with open('test.txt','r',encoding='utf8') as f1,open('test1.txt','w',encoding='utf8') as f2:
#     pass

with open('test.txt','w',encoding='utf8') as  f:
    f.write('-'.join(['广东省','广州市:黄浦区','深圳市']))
with open('test.txt','r',encoding='utf8') as f:
    for i in f:
        i.strip(':')
        print(i)

