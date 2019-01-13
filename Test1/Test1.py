# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Test1
   Description :
   Author :       Administrator
   date：          2019/1/13 0013
-------------------------------------------------
   Change Activity:
                   2019/1/13 0013:
-------------------------------------------------
"""
__author__ = 'Administrator'

import sys
reload(sys)
default_encoding="utf-8"
if(default_encoding!=sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

path="C:\Config\\global.properties"

from lib.PropertiesUtils import *


pro = parse(path)

print pro.get("path")

print  os.listdir("C:\\")

for item in os.listdir("C:\\"):
    #print item.decode("gb2312")
    #使用pip进行安装：pip install chardet
    import chardet
    #打印读物内容的编码格式
    #print chardet.detect(item)
    #打印读取内容
    print item.decode("gb2312")

    if os.path.isfile("C:\\"+item):
        print "This is a file: %s"%item.decode("gb2312")
        print "This is a file: " + item.decode("gb2312")
        print "This is a file: " + item

