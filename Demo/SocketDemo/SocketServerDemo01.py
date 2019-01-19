# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     SocketDemo01
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
Socket模块使用： Server 示例01--不支持多客户端
'''

if __name__ == '__main__':
    import socket

    sk = socket.socket()
    sk.bind(('127.0.0.1', 8000,))
    sk.listen(5)
    while True:
        conn, address = sk.accept()
        conn.sendall('Wellcome ！')
        while True:
            #ret = str(conn.recv(1024), encoding='utf-8')
            ret = str(conn.recv(1024))
            print(ret)
            if ret == 'q':
                break
            conn.sendall(ret + 'nice')
    sk.close()