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
Python+MySQLdb: 插入记录 示例
'''

from constants.MySQLDBCONSTANT import *


from com.mosorg.common.db.MySQLHelper import MySQLHelper
from vo.Account import Account

def add(sql,args=None):
    mySqlHelper = MySQLHelper()
    # 打开数据库连接
    conn = mySqlHelper.connetMySQL(host, user, pwd, dbname)
    #print  conn
    # 使用cursor()方法获取操作游标
    cursor = mySqlHelper.getCursor()
    #print cursor

    # 使用execute方法执行SQL语句
    #cursor.execute("use " + dbname)
    cursor.execute(sql,args)

    #提交事务
    conn.commit()

    # 关闭数据库连接
    cursor.close()
    conn.close()

def fetchall(sql,args=None):
    mySqlHelper = MySQLHelper()
    # 打开数据库连接
    conn = mySqlHelper.connetMySQL(host, user, pwd, dbname)
    #print  conn
    # 使用cursor()方法获取操作游标
    cursor = mySqlHelper.getCursor()
    #print cursor

    # 使用execute方法执行SQL语句
    #cursor.execute("use " + dbname)
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
    sql_insert = "INSERT INTO account (name,password) VALUES ('test11','test');"
    sql_insert1 = "INSERT INTO account (name,password) VALUES (%(name)s,%(password)s);"
    sql_update = "UPDATE account SET password= 'msmiles1' WHERE name = 'test';"
    sql_delete = "DELETE FROM account WHERE name = 'test';"
    # CAST(createtime AS CHAR) AS createtime  --在MySQL端处理日期类型数据，将datetime类型转字符串后再返回
    select_sql = "SELECT id, name, password,CAST(createtime AS CHAR) AS createtime FROM account;"
    select_sql1 = "SELECT id, name, password,CAST(createtime AS CHAR) AS createtime FROM account WHERE password=%(password)s;"

    print  "====dbname: " + dbname

    print  "==============sql_insert=======================: \n"
    add(sql_insert)

    print  "==============sql_insert1=======字典传参================: \n"

    import random
    # 生成0到100的随机数
    rannum = random.randint(0, 100)
    import time
    # 生成当前时间戳
    timenum = time.time()
    # 将两个数据变成字符串
    strrannum = str(rannum)
    print strrannum
    strtimenum = str(timenum)
    print strtimenum
    rantime = "".join((strrannum, strtimenum))
    print rantime

    account=Account()

    account.setName("rtest"+rantime)
    account.setPassword("test")
    account_dict={}
    account_dict["name"]=account.getName()
    account_dict["password"]=account.getPassword()
    print account_dict

    add(sql_insert1,account_dict)

    print  "==============fetchall select_sql1======字典传参=================: \n"
    fetchall(select_sql1, {'password': 'test'})