# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AccountManagerConsole
   Description :
   Author :       Administrator
   date：          2019/1/20 0020
-------------------------------------------------
   Change Activity:
                   2019/1/20 0020:
-------------------------------------------------
"""
from Demo.MySQLDemo.Service.impl.AccountManagerImpl import AccountManagerImpl
from Demo.MySQLDemo.UI.Menu import showMenu

__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''
AccountManager Console

'''

class AccountManagerConsole:

    def __init__(self):
        self.flag=False
        self.accountManager = AccountManagerImpl()

    def dealmenu(self):
        self.flag=True
        while self.flag:
            showMenu()
            select_menu = raw_input("请选择：")

            for case in switch(select_menu):
                if case('s'):
                    self.queryAccounts()
                    break
                if case('a'):
                    self.addAccount()
                    break
                if case('m'):
                    self.updateAccount()
                    break
                if case('d'):
                    self.deleteAccount()
                    break
                if case('q'):
                    self.exitSystem()
                    break
                if case():  # default
                    print "选择功能不支持..."
                    break
        print "Exit system success."


    def queryAccounts(self):
        print "Enter queryAccounts..."
        # CAST(createtime AS CHAR) AS createtime  --在MySQL端处理日期类型数据，将datetime类型转字符串后再返回
        self.select_sql = "SELECT id, name, password,CAST(createtime AS CHAR) AS createtime FROM account;"
        self.accountManager.queryAccounts(self.select_sql)

    def addAccount(self):
        print "Enter queryAccounts..."
        name = raw_input("请输入账号名称：")
        password = raw_input("请输入账号密码：")

        account_dict = {}
        account_dict["name"] = name
        account_dict["password"] = password

        sql_insert = "INSERT INTO account (name,password) VALUES (%(name)s,%(password)s);"
        self.accountManager.addAccount(sql_insert,account_dict)
        print "Add account [ "+name+" ] success."

        '''
        account=[]
        account.append(name)
        account.append(password)
        '''

    def updateAccount(self):
        print "Enter updateAccount..."
        old_name = raw_input("请输入账号名称：")
        new_name = raw_input("请输入账号新名称：")
        new_password = raw_input("请输入账号新密码：")

        account_dict = {}
        account_dict["new_name"] = new_name
        account_dict["new_password"] = new_password
        account_dict["old_name"] = old_name

        sql_update = "UPDATE account SET name= %(new_name)s,password= %(new_password)s WHERE name = %(old_name)s;"
        self.accountManager.updateAccount(sql_update,account_dict)
        print "Update account[ "+old_name+" ] success."

    def deleteAccount(self):
        print "Enter deleteAccount..."
        name = raw_input("请输入账号名称：")

        account_dict = {}
        account_dict["name"] = name

        sql_delete = "DELETE FROM account WHERE name = %(name)s;"
        self.accountManager.deleteAccount(sql_delete,account_dict)
        print "delete account[ "+name+" ] success."

    def exitSystem(self):
        print "Enter exitSystem..."
        self.flag=False
        print "Go to exit system."

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

if __name__ == '__main__':
    consoleService=AccountManagerConsole()

    consoleService.dealmenu()







