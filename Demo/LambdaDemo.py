# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LambdaDemo
   Description :
   Author :       Administrator
   date：          2019/1/17 0017
-------------------------------------------------
   Change Activity:
                   2019/1/17 0017:
-------------------------------------------------
"""
__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''
Lambda Demo
'''
a = lambda x,y:x+y
print a(4,10)



switch1 = {
        "a": lambda x: x * 2,
        "b": lambda x: x * 3,
        "c": lambda x: x ** x
    }
try:
    print  switch1["a"](6)
except KeyError as e:
    pass