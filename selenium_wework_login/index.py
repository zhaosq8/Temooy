#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/2 15:08
# @File: index.PY
# @Software: PyCharm
from selenium import webdriver
from selenium_wework_login.login import Login
from selenium_wework_login.register import Register


class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')
        self._driver.maximize_window()

    def goto_login(self):
        # click login
        self._driver.find_element_by_link_text("企业登录").click()
        return Login(self._driver)

    def goto_register(self):
        # click register
        self.driver.find_element_by_link_text("立即注册").click()
        return Register(self._driver)
