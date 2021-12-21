#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/20 15:19
# @File: index.PY
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By

from demo.selenium_wework_login.login import Login
from demo.selenium_wework_login.register import Register


class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')
        self._driver.maximize_window()

    def goto_login(self):
        # click login
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_registerBtn').click()
        return Login()

    def goto_register(self):
        # click register
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register()
