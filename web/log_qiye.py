#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/2 9:17
# @File: log_qiye.PY
# @Software: PyCharm
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():

    def setup_method(self, method):

        # options = Options()
        # options.debugger_address = "127.0.0.1:9000"
        # self.driver = webdriver.Chrome(options=options)
        # self.vars = {}
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()

    def teartdown_method(self, method):
        self.driver.quit()

    def test_one(self):
        self.driver.find_element_by_link_text("企业登录").click()
        sleep(10)
        print(self.driver.get_cookies())
        sleep(5)