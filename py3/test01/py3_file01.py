#!/usr/bin/env python
# encoding: utf-8

"""
@Version: Python 3.6.2
@Author: zwl
@File: py3_file01.py
@Time: 2017/07/24 12:55
"""
'''
class Foo:
    def Bar(self):
        print('Bar')

    def Hello(self,name):
        print('i am %s' %name)

obj=Foo()
obj.Bar()
obj.Hello('test')
'''
'''
class Test:
    def __init__(self,name,sex,age):
        self.name1=name
        self.sex1=sex
        self.age1=age


    def kanchai(self):
        print(self.name1,self.age1,'岁，性别：',self.sex1,'上山去砍柴')
    def dabaojian(self):
        print(self.name1,self.age1,'岁，性别：',self.sex1,'去大保健')
obj01=Test('小米','男',18)
obj01.kanchai()
obj01.dabaojian()
'''

class Game:
    def __init__(self,name,sex,age,fig):
        self.name=name
        self.sex=sex
        self.age=age
        self.fig=fig

    def grassland(self):
        '''在草丛'''
        self.fig=self.fig - 200

    def myself(self):
        '''自我修养'''
        self.fig=self.fig - 100
    def together(self):
        '''多人战斗'''
        self.fig=self.fig - 500

    def Print(self):
        temp = "姓名：%s;性别：%s;年龄：%s;战斗力：%s;" % (self.name,self.sex,self.age,self.fig)
        print(temp)

Cang=Game('cangjingk','女',18,2000)
TX=Game('Teng','女',29,2500)

Cang.grassland()
TX.myself()
Cang.Print()
TX.Print()











