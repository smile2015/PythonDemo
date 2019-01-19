# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Version
   Description :
   Author :       Administrator
   date：          2019/1/20 0020
-------------------------------------------------
   Change Activity:
                   2019/1/20 0020:
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
用户管理系统 V 1.0
'''

if __name__ == '__main__':
    print "用户管理系统 V 1.0"