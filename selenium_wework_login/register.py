#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/2 15:12
# @File: register.PY
# @Software: PyCharm
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        sleep(5)
        self._driver.find_element(By.ID, 'corp_name').send_keys("hello11")
        self._driver.find_element(By.ID, 'manager_name').send_keys('helll')
        sleep(5)
        self._driver.quit()
        return True