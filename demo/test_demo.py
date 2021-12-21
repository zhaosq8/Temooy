#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/15 16:12
# @File: test_demo.PY
# @Software: PyCharm
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():

    def setup_method(self, method):
        # options = Options()
        # options.debugger_address = '127.0.0.1:9332'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # print(3333)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        # sleep(15)
        # print(self.driver.get_cookies())
        # 使用cookie需要在之前请求一下网址
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # shelve 相当于一个小型的数据库
        db = shelve.open("cookies")
        #db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            # 'cookis'中如果存在expiry可能会报错
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)
        db.close()

