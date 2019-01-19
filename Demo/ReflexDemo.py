# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ReflexDemo
   Description :
   Author :       Administrator
   date：          2019/1/19 0019
-------------------------------------------------
   Change Activity:
                   2019/1/19 0019:
-------------------------------------------------
"""
from vo.Account import Account

__author__ = 'Administrator'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''
【转载】反射示例
'''

if __name__ == '__main__':
    obj = Account()
    obj.setId(1000)
    obj.setName("Tom")
    obj.setPassword("GDfds")
    obj.setCreatetime("2019-01-19 23:41:54")
    # 获取成员
    ret = getattr(obj, 'toString')  # 获取的是个对象
    r = ret()
    print(r)
    # 检查成员
    ret = hasattr(obj, 'toString')  # 因为有func方法所以返回True
    print(ret)
    # 设置成员
    print(obj.name)  # 设置之前为:abc
    ret = setattr(obj, 'name', "gddd")
    print(obj.name)  # 设置之后为:19
    # 删除成员
    print(obj.name)  # abc
    delattr(obj, 'name')
    print(obj.name)  # 报错