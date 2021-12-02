#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/2 15:11
# @File: login.PY
# @Software: PyCharm
from selenium.webdriver.remote.webdriver import WebDriver
from selenium_wework_login.register import Register


class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        # click register
        self._driver.find_element_by_link_text("企业注册").click()
        return Register(self._driver)
