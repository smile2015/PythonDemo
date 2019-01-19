# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     SocketClientDemo01
   Description :
   Author :       Administrator
   date：          2019/1/20 0020
-------------------------------------------------
   Change Activity:
                   2019/1/20 0020:
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
Socket模块使用： Client 示例01
'''

if __name__ == '__main__':
    import socket

    obj = socket.socket()

    obj.connect(('127.0.0.1', 8000,))

    while True:
        ret_str = str((obj.recv(1024)))
        print(ret_str)
        content = raw_input('请输入要发送的内容:')
        if content == 'q':
            obj.sendall(content)
            break
        else:
            obj.sendall(content)
    obj.close()