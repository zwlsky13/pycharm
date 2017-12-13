#!/usr/bin/env python
# encoding: utf-8

"""
@Version: Python 3.6.2
@Author: zwl
@File: py3_xml.py
@Time: 2017/12/13 18:12
"""

import xml.etree.ElementTree as ET

tree=ET.parse("xmltest.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.attrib)

#只遍历year 节点

for node in root.iter('year'):

    print(node.tag,node.text)

#---------------------------------------


