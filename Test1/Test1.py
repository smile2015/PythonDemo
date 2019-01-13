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
sys.setdefaultencoding('utf8')

path="C:\Config\\global.properties"

from lib.PropertiesUtils import *


pro = parse(path)

print pro.get("path")
