# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MySQLDBCONSTANT
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
MySQL数据库配置数据
'''

#cmd 连接数据库命令：mysql -uroot -p
host="localhost"
port=3306
user="root"
pwd=""
dbname="test"
encoding="utf8"
