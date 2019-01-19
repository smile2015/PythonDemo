# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Account
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

'''

class Account:

    def __init__(self):
        self.id=0
        self.name=None
        self.password=None
        self.createtime=None

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getCreatetime(self):
        return self.createtime

    def setCreatetime(self, createtime):
        self.createtime = createtime

    def toString(self):
        return "Account[ID："+str(self.getId())+", name："+self.getName()+", password："+self.getPassword()+", createtime："+self.getCreatetime()+"]"



if __name__ == '__main__':
    pass