# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     DefineExceptionDemo
   Description :
   Author :       Administrator
   date：          2019/1/19 0019
-------------------------------------------------
   Change Activity:
                   2019/1/19 0019:
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
自定义异常示例
'''


class MyEception(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message




if __name__ == '__main__':
    try:
        raise MyEception('自定义异常示例')
    except MyEception as e:
        print e
