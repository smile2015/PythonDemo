# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     FileDemo
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
网上转载文件写示例，内容为随机数+当前时间戳
'''



if __name__ == '__main__':
    import random
    import time

    # 实战，生成一个包含时间戳和随机数的字符串
    # 生成0到100的随机数
    rannum = random.randint(0, 100)
    # 生成当前时间戳
    timenum = time.time()
    # 将两个数据变成字符串
    strrannum = str(rannum)
    strtimenum = str(timenum)
    # 两个字符串链接起来
    rantime = "".join((strrannum, strtimenum))
    # 将字符换保存在一个文件中
    filert = open("rantime.txt", "a+")
    filert.write(rantime)
    filert.write("\n")
    filert.flush()
    filert.close()