# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AccountManager
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
Account  Manager
'''

#定义父类AccountManager
class AccountManager(object): #假设这就是一个接口，接口名可以随意定义，所有的子类不需要实现在这个类中的函数
    def __init__(self):
        pass

    def addAccount(self,sql, args=None):
        pass

    def queryAccounts(self,sql, args=None):
        pass

    def updateAccount(self,sql, args=None):
        pass

    def deleteAccount(self,sql, args=None):
        pass

if __name__ == '__main__':
    pass