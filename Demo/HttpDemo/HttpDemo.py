# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     HttpDemo
   Description :
   Author :       MyPC
   date：          2019/2/14
-------------------------------------------------
   Change Activity:
                   2019/2/14:
-------------------------------------------------
"""
from com.mosorg.common.http.HttpHelper import HttpHelper

__author__ = 'MyPC'

import sys

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''

'''
import httplib
import urllib

if __name__ == '__main__':
    host = '192.168.1.100'
    port = 8888
    strict = False
    timeout = 10
    method = 'GET'
    url = '/index'
    content={
        '@username': 'New_Day2009',
        '@password': 'H71QemYbuWm2rQgxd4wUzIKHdxh9JIHDcyI5+H6D/pedmnFuJmKjBKT5tXK270WNYc1mThSpOZPwz3X9SpZLDWzBVdopPSOHSwrBXtCv1lVW/Yu96YTXrXM48JFs2+MPdoUkx9fvp7E7eYDFptutqkJOmLAtc8GVsT4ykBExHlI='
    }
    body = ''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    protocol = 0

    httpDemo=HttpHelper(host, port, strict, timeout)
    httpDemo.sendMsg(method,url,body,headers,protocol)
    print httpDemo.result

    print "============================="

    method = 'POST'
    url = '/AddUser'
    content = {
        '@username': 'New_Day2009',
        '@password': 'H71QemYbuWm2rQgxd4wUzIKHdxh9JIHDcyI5+H6D/pedmnFuJmKjBKT5tXK270WNYc1mThSpOZPwz3X9SpZLDWzBVdopPSOHSwrBXtCv1lVW/Yu96YTXrXM48JFs2+MPdoUkx9fvp7E7eYDFptutqkJOmLAtc8GVsT4ykBExHlI='
    }
    body = ''

    httpDemo = HttpHelper(host, port, strict, timeout)
    httpDemo.sendMsg(method, url, body, headers, protocol)
    print httpDemo.result

