# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AccountManagerImpl
   Description :
   Author :       Administrator
   date：          2019/1/20 0020
-------------------------------------------------
   Change Activity:
                   2019/1/20 0020:
-------------------------------------------------
"""
from Demo.MySQLDemo.Service import AccountManager
from com.mosorg.common.db.MySQLHelper import MySQLHelper
from constants.MySQLDBCONSTANT import *
from vo.Account import Account

__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''
Account  Manager  impl

'''

class AccountManagerImpl:

    def __init__(self):
        self.mySqlHelper = MySQLHelper()

    def addAccount(self,sql, args=None):
        try:
            # 打开数据库连接
            self.mySqlHelper.connetMySQL(host, user, pwd, dbname)
            # 使用execute方法执行SQL语句
            self.mySqlHelper.execute(sql,args)
            self.mySqlHelper.commit()
            self.mySqlHelper.closeCursor()
            self.mySqlHelper.closeConnet()
            return True
        except Exception as e:
            print str(e)
            self.mySqlHelper.closeCursor()
            self.mySqlHelper.closeConnet()
            raise "Add account fail."


    def queryAccounts(self,sql, args=None):
        try:
            # 打开数据库连接
            self.mySqlHelper.connetMySQL(host, user, pwd, dbname)

            rs = self.mySqlHelper.query(sql,args)

            accountList = []
            for row in rs:
                # print row[0]
                account = Account()
                account.setId(row[0])
                account.setName(row[1])
                account.setPassword(row[2])
                account.setCreatetime(row[3])
                accountList.append(account)


            for account in accountList:
                print account.toString()


            self.mySqlHelper.closeCursor()
            self.mySqlHelper.closeConnet()
            return accountList
        except Exception as e:
            print str(e)
            self.mySqlHelper.closeCursor()
            self.mySqlHelper.closeConnet()
            raise "Query account fail."

    def updateAccount(self,sql, args=None):
        try:
            # 打开数据库连接
            self.mySqlHelper.connetMySQL(host, user, pwd, dbname)
            # 使用execute方法执行SQL语句
            self.mySqlHelper.execute(sql,args)
            self.mySqlHelper.commit()
            self.mySqlHelper.closeCursor()
            self.mySqlHelper.closeConnet()
            return True
        except Exception as e:
            print str(e)
            self.mySqlHelper.closeCursor()
            self.mySqlHelper.closeConnet()
            raise "Update account fail."

    def deleteAccount(self,sql, args=None):
        try:
            # 打开数据库连接
            self.mySqlHelper.connetMySQL(host, user, pwd, dbname)
            # 使用execute方法执行SQL语句
            self.mySqlHelper.execute(sql,args)
            self.mySqlHelper.commit()
            self.mySqlHelper.closeCursor()
            self.mySqlHelper.closeConnet()
            return True
        except Exception as e:
            print str(e)
            self.mySqlHelper.closeCursor()
            self.mySqlHelper.closeConnet()
            raise "Delete account fail."

if __name__ == '__main__':
    pass