# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Menu
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
Account manager home papge

'''

def showMenu():
    print " ----------------------------------------"
    print "|        欢迎使用用户管理系统            |"
    print "|  (Welcome to use user manager system)  |"
    print "|----------------------------------------|"
    print "|  [s] 查询用户列表(Query Account List)  |"
    print "|  [a] 新增用户(Add New Account)         |"
    print "|  [m] 修改用户(Modify Account)          |"
    print "|  [d] 删除用户(Delete Account)          |"
    print "|  [q] 退出系统(Exit System)             |"
    print " ----------------------------------------"


if __name__ == '__main__':
    user_select=showMenu()
