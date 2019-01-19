# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     FuncDemo
   Description :
   Author :       Administrator
   date：          2019/1/16 0016
-------------------------------------------------
   Change Activity:
                   2019/1/16 0016:
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
 函数参数
'''

def show(item):
    print "========函数参数=========="
    print item

item = "Tom"
show(item)

'''
 函数可变参数，可传递列表作为参数
'''

def show1(*arg):
    print "========函数可变参数，可传递列表作为参数=========="
    for item in arg:
        print item
    for item in xrange(10):
        print item

#传递列表作为参数
itemlist=['Tom','Jhon']
show1(*itemlist)

#传递元组作为参数
itemlist1=('Tom','Jhon')
show1(*itemlist1)

'''
 函数可变参数，可传递字典作为参数
'''

def show2(**kargs):
    print "========函数可变参数，可传递字典作为参数=========="
    for item in kargs.items():
        print item

#传递字典作为参数
itemdict={'Tom':"23",'Jhon':"43"}
show2(**itemdict)

