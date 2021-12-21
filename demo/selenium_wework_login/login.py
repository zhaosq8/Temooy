#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/20 15:21
# @File: login.PY
# @Software: PyCharm
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from demo.selenium_wework_login.register import Register


class Login:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        # click registe
        self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register()