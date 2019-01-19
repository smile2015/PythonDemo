# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     SocketServerDemo02
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
socketserver 模块使用：实现多线程，支持多客户端(未调试)

'''

if __name__ == '__main__':
    import socketserver


    class Mysocket(socketserver.BaseRequestHandler):  # 继承socketserver.BaseRequestHandler类

        def handle(self):  # 重写 handle方法
            conn = self.request  # self.request 指客户端的连接
            conn.sendall(bytes('Wellcome！', encoding='utf-8'))
            while True:
                ret = str(conn.recv(1024), encoding='utf-8')
                print(ret)
                if ret == 'q':
                    break
                conn.sendall(bytes(ret + 'nice', encoding='utf-8'))


    if __name__ == '__main__':
        obj = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), Mysocket)
        obj.serve_forever()