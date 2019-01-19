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
from com.mosorg.common.file.FileUtils import FileUtils
from com.mosorg.common.file.PropertiesUtils import PropertiesUtils

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
pwd="test@root"
dbname=""
encoding="utf8"

#初始化数据库配置信息
def init_db_constants():
    db_config_path = "config/db.properties"
    fileUtils=FileUtils()
    db_config_path=fileUtils.getCurrentPath()+"/config/db.properties"
    print db_config_path
    pro = PropertiesUtils(db_config_path)
    host = pro.get("host")
    print host
    port = int(pro.get("port"))
    print port
    user = pro.get("user")
    print user
    pwd = pro.get("pwd")
    print pwd
    dbname = pro.get("dbname")
    print dbname
    encoding = pro.get("encoding")
    print encoding

init_db_constants()