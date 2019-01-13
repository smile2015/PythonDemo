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
    print item.decode("gb2312")
