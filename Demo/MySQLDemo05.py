# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MySQLDemo02
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
Python+MySQLdb: 删除记录 示例
'''

from constants.MySQLDBCONSTANT import *


from com.mosorg.common.db.MySQLHelper import MySQLHelper
from vo.Account import Account

def delete(sql,args=None):
    mySqlHelper = MySQLHelper()
    # 打开数据库连接
    conn = mySqlHelper.connetMySQL(host, user, pwd)
    #print  conn
    # 使用cursor()方法获取操作游标
    cursor = mySqlHelper.getCursor()
    #print cursor

    # 使用execute方法执行SQL语句
    cursor.execute("use " + dbname)
    cursor.execute(sql,args)

    #提交事务
    conn.commit()

    # 关闭数据库连接
    cursor.close()
    conn.close()

def fetchall(sql,args=None):
    mySqlHelper = MySQLHelper()
    # 打开数据库连接
    conn = mySqlHelper.connetMySQL(host, user, pwd)
    #print  conn
    # 使用cursor()方法获取操作游标
    cursor = mySqlHelper.getCursor()
    #print cursor

    # 使用execute方法执行SQL语句
    cursor.execute("use " + dbname)
    cursor.execute(sql,args)

    accountList = []

    res = cursor.fetchall()
    #print res
    for row in res:
        #print row[0]
        account = Account()
        account.setId(row[0])
        account.setName(row[1])
        account.setPassword(row[2])
        account.setCreatetime(row[3])
        accountList.append(account)

    for account in accountList:
        print account.toString()

    # 关闭数据库连接
    cursor.close()
    conn.close()

if __name__ == '__main__':
    sql_insert = "INSERT INTO account (name,password) VALUES ('test42','test');"
    sql_insert1 = "INSERT INTO account (name,password) VALUES (%(name)s,%(password)s);"
    sql_update = "UPDATE account SET password= 'testmodify' WHERE name = 'test42';"
    sql_update1 = "UPDATE account SET password= %(password)s WHERE name = %(name)s;"
    sql_delete = "DELETE FROM account  WHERE name = 'test1231';"
    sql_delete1 = "DELETE FROM account WHERE name = %(name)s;"
    sql_delete2 = "DELETE FROM account WHERE name = %s;"
    select_sql = "SELECT id, name, password,CAST(createtime AS CHAR) AS createtime FROM account;"
    select_sql1 = "SELECT id, name, password,CAST(createtime AS CHAR) AS createtime FROM account WHERE password=%(password)s;"

    print  "====dbname: " + dbname

    print  "==============sql_delete=======================: \n"
    delete(sql_delete)

    print  "==============sql_delete1=======字典传参================: \n"

    account=Account()

    account.setName("test121")
    account.setPassword("testmodify")
    account_dict={}
    account_dict["name"]=account.getName()
    print account_dict

    delete(sql_delete1,account_dict)

    print  "==============fetchall select_sql1======字典传参=================: \n"
    fetchall(select_sql)

    print  "==============sql_delete1=======列表传参================: \n"

    account = Account()

    account.setName("test11")
    account.setPassword("testmodify")
    params = []
    params.append(account.getName())
    print params

    delete(sql_delete2, params)

    print  "==============fetchall select_sql1======字典传参=================: \n"
    fetchall(select_sql)