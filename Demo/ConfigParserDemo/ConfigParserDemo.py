# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ConfigParserDemo
   Description :
   Author :       MyPC
   date：          2019/2/13
-------------------------------------------------
   Change Activity:
                   2019/2/13:
-------------------------------------------------
"""
from com.mosorg.common.file.readConfig import ReadConfig

__author__ = 'MyPC'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''

'''
import os
if __name__ == '__main__':
    #proDir = os.path.split(os.path.realpath(__file__))[0]
    #configPath = os.path.join(proDir, "..\\..\\config\\config.ini")
    #s = ReadConfig(configPath)

    import sys

    print sys.argv[0]

    import re, os

    # 测试
    paths = ['D:\\code\\GitHub\\PythonDemo\\config', 'home/Python/Project/', 'c:/balabala/Python/Project/']
    for path in paths:
        pj_dir = re.match('.*config', path)
        print(pj_dir.group())

    # 在子文件下就应该这样用
    print(re.match('(.*\{sep}config)\{sep}'.format(sep=os.sep), __file__).group(1))

