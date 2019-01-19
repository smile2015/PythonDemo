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
from com.mosorg.common.db.MySQLHelper import MySQLHelper

__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''

'''

mySqlHelper=MySQLHelper()

#cmd 连接数据库命令：mysql -uroot -p
host="localhost"
port=3306
user="root"
pwd="MINGtian2010"
dbname="test"
encoding="utf8"
mySqlHelper.connetMySQL(host,user,pwd,dbname)
print  mySqlHelper.conn
