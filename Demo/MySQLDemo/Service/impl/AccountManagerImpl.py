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
1、使用字典作为MySQL连接参数
2、使用了类的内置行数进行连接MySQL和断开MySQL，减少打开MySQL次数

'''

class AccountManagerImpl:

    def __init__(self):
        self.mySqlHelper = MySQLHelper()
        self.connect()

    def __str__(self):
        return "This is AccountManagerImpl class"

    def __del__(self):  # 回收，脚本执行的最后执行
        print "Del……"  # 显示执行顺序
        self.disConnet()


    def connect(self):
        '''
        打开数据库连接
        :return: 
        '''
        # 下面连个字典都可行
        # conn_dict=dict(host=host,user=user,passwd=pwd,db=dbname,port=3306,charset="utf8")
        conn_dict = dict(host=host, user=user, passwd=pwd, db=dbname)
        # 打开数据库连接（改成使用字典进行连接参数传递）
        return self.mySqlHelper.connetMySQLArgsByDict(conn_dict)

    def disConnet(self):
        '''
        断开数据库连接
        :return: 
        '''
        self.mySqlHelper.closeCursor()
        self.mySqlHelper.closeConnet()
        print "Close connetction success."

    def addAccount(self,sql, args=None):
        '''
        新增账号
        :param sql: SQL语句
        :param args:  字典/列表类型参数，根据SQL参数化时构造场景而定。SQL语句参数化场景需要传值，其他场景不传，默认使用None
        :return: 新增成功返回True，否则报异常
        '''
        try:
            # 使用execute方法执行SQL语句
            self.mySqlHelper.execute(sql,args)
            self.mySqlHelper.commit()
            return True
        except Exception as e:
            print str(e)
            raise "Add account fail."


    def queryAccounts(self,sql, args=None):
        '''
        查询账号信息列表
        :param sql: SQL语句
        :param args:  字典/列表类型参数，根据SQL参数化时构造场景而定。SQL语句参数化场景需要传值，其他场景不传，默认使用None
        :return: 返回账号信息列表
        '''
        try:
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

            return accountList
        except Exception as e:
            print str(e)
            raise "Query account fail."

    def updateAccount(self,sql, args=None):
        '''
        修改账号信息
        :param sql: SQL语句
        :param args:  字典/列表类型参数，根据SQL参数化时构造场景而定。SQL语句参数化场景需要传值，其他场景不传，默认使用None
        :return: 新增成功返回True，否则报异常
        '''
        try:
            # 使用execute方法执行SQL语句
            self.mySqlHelper.execute(sql,args)
            self.mySqlHelper.commit()
            return True
        except Exception as e:
            print str(e)
            raise "Update account fail."

    def deleteAccount(self,sql, args=None):
        '''
        删除账号信息
        :param sql: SQL语句
        :param args:  字典/列表类型参数，根据SQL参数化时构造场景而定。SQL语句参数化场景需要传值，其他场景不传，默认使用None
        :return: 新增成功返回True，否则报异常
        '''
        try:
            # 使用execute方法执行SQL语句
            self.mySqlHelper.execute(sql,args)
            self.mySqlHelper.commit()
            return True
        except Exception as e:
            print str(e)
            raise "Delete account fail."

if __name__ == '__main__':
    pass