# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MySQLDemo01
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
Python+MySQLdb: fetchone 示例
'''

from constants.MySQLDBCONSTANT import *


from com.mosorg.common.db.MySQLHelper import MySQLHelper

def fetchone(sql):
    mySqlHelper = MySQLHelper()
    # 打开数据库连接
    conn = mySqlHelper.connetMySQL(host, user, pwd, dbname)
    #print  conn
    # 使用cursor()方法获取操作游标
    cursor = mySqlHelper.getCursor()
    #print cursor

    # 使用execute方法执行SQL语句
    #cursor.execute("use " + dbname)
    cursor.execute(select_sql)


    # 使用 fetchone() 方法获取一条数据
    rs = cursor.fetchone()

    print "=========rs=========="

    print rs

    print "=========item=========="

    for item in rs:
        print item

    # 关闭数据库连接
    cursor.close()
    conn.close()

if __name__ == '__main__':
    sql_insert = "INSERT INTO account (name,password) VALUES ('test','test');"
    sql_update = "UPDATE account SET password= 'msmiles1' WHERE name = 'test';"
    sql_delete = "DELETE FROM account WHERE name = 'test';"
    # CAST(createtime AS CHAR) AS createtime  --在MySQL端处理日期类型数据，将datetime类型转字符串后再返回
    select_sql = "SELECT id, name, password,CAST(createtime AS CHAR) AS createtime FROM account;"


    print  "====dbname: " + dbname

    print  "==============fetchone=======================: \n"
    fetchone(select_sql)