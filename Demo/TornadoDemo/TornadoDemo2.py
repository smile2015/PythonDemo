# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     TornadoDemo
   Description :
   Author :       MyPC
   date：          2019/2/14
-------------------------------------------------
   Change Activity:
                   2019/2/14:
-------------------------------------------------
"""
__author__ = 'MyPC'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''

'''

import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
from tornado.escape import json_decode,json_encode

import tornado.httpserver
import tornado.options
from tornado.options import define,options


#解决js跨域请求问题
class BaseHandler(RequestHandler):
     def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

class IndexHandler(BaseHandler):
   def get(self):
      result={}
      content = []
      content.append({'id': 1, 'name': 'fdsafdsa'})
      result["total"] = 1000
      result["rows"] = content
      result["status"] = "true"
      result["code"] = 200
      print json_encode(result)
      self.write(json_encode(result))

class AddHandler(BaseHandler):
    def post(self):
      time=self.get_argument('time',None)
      result={}

      result["result"]="success"
      result["status"]="true"
      result["code"]=200
      self.write(json_encode(result))

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r'/AddUser',AddHandler)
])


define("port",default=8888,help="run on port",type=int)

if __name__=="__main__":
   tornado.options.parse_command_line()
   application.listen(options.port)
   tornado.ioloop.IOLoop.instance().start()
