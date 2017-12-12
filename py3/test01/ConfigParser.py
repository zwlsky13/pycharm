#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@version: Python 3.6.2
@author: zwl
@Project: py3
@file: ConfigParser.py
@time: 2017/10/31 23:08
"""

import configparser
config=configparser.ConfigParser()
# config["DEFAULT"] = { 'ServerAliveInterval': '45',
#                         'Compression':'yes',
#                         'CompressionLevel':'9'}
# config['bitbucket.org']={}
# config['bitbucket.org']['user']='hg'
# config['topsecret.server.com']={}
# topsecret=config['topsecret.server.com']
# topsecret['Host Port']='50022'
# topsecret['Forwardx11']='no'
# config['DEFAULT']['ForwardX11']='yes'
# with open ('config.ini','w') as configfile:
#     config.write(configfile)



config.read('config.ini')
print(config.sections())
print(config.defaults())
for i in config['topsecret.server.com']: print(i)
print(config['topsecret.server.com']['host port'])

print(config.items('topsecret.server.com'))