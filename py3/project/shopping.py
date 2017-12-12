#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
@Version: Python 3.6.2
@Author: ZWL
@Project: py3
@File: shopping.py
@Time: 2017/08/03 14:46
"""
product_shop=[]
args=True
arg1=True
while arg1:
    Salary = input('请输入你的工资：')
    if not Salary.isdigit():
        print('你输入的不是有效数字，请重新输入数字！')
    else:
        arg1=False
        Salary=int(Salary)
        Balance = Salary
while args:
    Menu='''
    ----------The Menu info----------
    1、iphone 7(128g)            5400
    2、iphone 7 plus(128g)       6400
    3、mac book                  9000
    4、coffee                    32
    5、python book               80
    6、bicycle                   1500
    ---------------------------------
    你目前的余额为：%s
    '''% (Balance)
    product_list=[
        ('iphone 7',5400),
        ('iphone 7 plus',6400),
        ('mac book',9000),
        ('coffee',32),
        ('python book',80),
        ('bicycle',1500)
    ]

    print(Menu)
    if  len(product_shop) > 0:#购买之后显示的购物车
        print("你目前已购买：",product_shop)
        ask = input("是否继续购物,结算退出请输入（N/n）")
        if ask == 'n' or ask == 'N':
            print('结算退出,你的工资为：%s,你目前已购买的商品：%s,剩余余额为：%s'%(Salary,product_shop,Balance))
            break
    arg2=True
    while arg2:
        shop_num = input("请输入你要购买的商品编号：")
        if not shop_num.isdigit():
            print('你输入的不是有效数字，请重新输入数字！')
        else:
            shop_num=int(shop_num)
            arg2=False
    if shop_num>0 and shop_num <=len(product_list):     #判断是否在列表里
        if Balance>=product_list[shop_num-1][1]:        #求出他的余额
            Balance=Balance-product_list[shop_num-1][1]
            product_shop.append(product_list[shop_num-1][0])

        else:
            print("余额不足，剩余：%s"%Balance)
    else:
        print("输入不是有效数字.")



