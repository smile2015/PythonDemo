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
Python+MySQLdb: fetchall 示例
'''

from constants.MySQLDBCONSTANT import *


from com.mosorg.common.db.MySQLHelper import MySQLHelper
from vo.Account import Account




def fetchall(sql,args=None):
    #下面连个字典都可行
    #conn_dict=dict(host=host,user=user,passwd=pwd,db=dbname,port=3306,charset="utf8")
    conn_dict = dict(host=host, user=user, passwd=pwd, db=dbname)
    mySqlHelper = MySQLHelper()
    # 打开数据库连接
    conn = mySqlHelper.connetMySQLArgsByDict(conn_dict)
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
    sql_insert = "INSERT INTO account (name,password) VALUES ('test','test');"
    sql_update = "UPDATE account SET password= 'msmiles1' WHERE name = 'test';"
    sql_delete = "DELETE FROM account WHERE name = 'test';"
    # CAST(createtime AS CHAR) AS createtime  --在MySQL端处理日期类型数据，将datetime类型转字符串后再返回
    select_sql = "SELECT id, name, password,CAST(createtime AS CHAR) AS createtime FROM account;"
    select_sql1 = "SELECT id, name, password,CAST(createtime AS CHAR) AS createtime FROM account WHERE password=%(password)s;"

    print  "====dbname: " + dbname

    print  "==============fetchall=======================: \n"
    fetchall(select_sql)

    print  "==============fetchall======字典传参=================: \n"
    fetchall(select_sql1, {'password': 'test'})