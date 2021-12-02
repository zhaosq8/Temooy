#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/11/24 9:52
# @File: web_demo.PY
# @Software: PyCharm
from selenium import webdriver
from time import sleep


class TestHogewozi(object):

    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(6)
        self.driver.quit()

    def test_hgwz(self):
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su").click()