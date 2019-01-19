# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MySQLHeperTest
   Description :
   Author :       Administrator
   date：          2019/1/19 0019
-------------------------------------------------
   Change Activity:
                   2019/1/19 0019:
-------------------------------------------------
"""
import MySQLdb

from MySQLDBCONSTANT import *
from com.mosorg.common.db.MySQLHelper import MySQLHelper

__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''
MySQLHelper类测试
'''

def queryMySQL():
    # 把一个事务放到一个try块里，如果出现异常就回滚

    try:
        print "=======statt"
        mySqlHelper.execute(sql_insert)
        print "=======statt1"

        mySqlHelper.execute(sql_update)
        print "=======statt2"

        mySqlHelper.execute(sql_delete)
        print "=======statt3"

        # 格式化增删改后的数据查出来
        mySqlHelper.execute(select_sql)
        print "=======statt"
        rs = mySqlHelper.fetchall()
        for row in rs:
            print "id=%d, name=%s, password=%s, createtime=%s" % row

        mySqlHelper.closeConnet()

    except Exception as e:
        print "=======Exception"
        mySqlHelper.conn.rollback()  # 若有异常就回滚
        mySqlHelper.closeConnet()

if __name__ == '__main__':

    sql_insert = "INSERT INTO account (name,password) VALUES ('test','test');"
    sql_update = "UPDATE account SET password= 'msmiles1' WHERE name = 'test';"
    sql_delete = "DELETE FROM account WHERE name = 'test';"
    select_sql = "SELECT * FROM account;"

    mySqlHelper = MySQLHelper()
    # 打开数据库连接
    _conn =mySqlHelper.connetMySQL(host, user, pwd)
    print  _conn
    # 使用cursor()方法获取操作游标
    _cursor=mySqlHelper.getCursor()
    print _cursor
    print  "====dbname"+db_name

    # 使用execute方法执行SQL语句
    _cursor.execute("use ?",[db_name])
    _cursor.execute(select_sql)

    # 使用 fetchone() 方法获取一条数据
    data = _cursor.fetchone()

    print data

    # 关闭数据库连接
    mySqlHelper.closeConnet()

    '''
    rs = mySqlHelper.execute(select_sql)
    for row in rs:
        print "id=%d, name=%s, password=%s, createtime=%s" % row
        '''

