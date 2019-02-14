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
import os

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
#初始化数据库配置信息
db_config_path = "/../config/db.properties"
fileUtils=FileUtils()
#db_config_path=fileUtils.getCurrentPath()+"/../config/db.properties"
#work_dir = os.path.dirname(os.path.abspath(__file__))
#db_config_path = os.path.join(work_dir,'config/db.properties')
db_config_path = os.path.join('D:/code/GitHub/PythonDemo/config/db.properties')
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