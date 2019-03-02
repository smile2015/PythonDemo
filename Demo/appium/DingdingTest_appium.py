# coding=UTF-8
"""
-------------------------------------------------
   File Name：     DingdingTest_appium
   Description :
   Author :       MyPC
   date：          2019/3/2
-------------------------------------------------
   Change Activity:
                   2019/3/2:
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

from time import sleep
import unittest

import logging
from appium import webdriver
from constants.AppiumData import *



class Test_appium(unittest.TestCase):
    def setUp(self):
        logging.info("Test_appium.....setUp")

        # 启动APK应用
        # appium的服务，查看地方：打开已经安装的appium，点击“设置”查看端口
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=desired_caps)
        sleep(40)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        # 退出
        self.driver.quit()

    def test_appium_01(self):
        pass


if __name__ == '__main__':
    unittest.main()