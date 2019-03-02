# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AppiumData
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


from appium import webdriver
import time

desired_caps = {}
#需要测试的平台---只分为Andriod和IOS
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
#当前的设备名称---如果只有一个设备连接了电脑，则可以随便写
#手机的串号，手机usb连接电脑，使用adb devices即可查看此串号，复制粘贴此处即可
desired_caps['deviceName'] = '127.0.0.1:6555'
#当前的输入文字编码
desired_caps['unicodeKeyboard'] = True
#输入文字时，不打开手机的键盘
desired_caps["resetKeyboard"] = True
#设置Appium的等待时间
desired_caps["newCommandTimeout"]=180
#可以直接安装改APK
#     desired_caps['app'] = 'F:\\workspace\\Appium\\apps\\sample-code-master\\app\\dingding_456.apk'
#APK的包名
#打开应用的包名
#进入目录D:\androidsdk\build-tools\28.0.3，使用命令查看：D:\androidsdk\build-tools\28.0.3>aapt dump badging D:\dingding_456.apk
desired_caps['appPackage'] = 'com.alibaba.android.rimet'
#应用的活动名称
#进入目录D:\androidsdk\build-tools\28.0.3，使用命令查看：D:\androidsdk\build-tools\28.0.3>aapt dump badging D:\dingding_456.apk
desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
#启动APK应用
#appium的服务，查看地方：打开已经安装的appium，点击“设置”查看端口
#driver = webdriver.Remote(command_executor = 'http://127.0.0.1:4723/wd/hub',desired_capabilities = desired_caps)
#time.sleep(35)
#退出应用
#driver.quit()
