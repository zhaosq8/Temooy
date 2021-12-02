#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/2 16:06
# @File: add_member.PY
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_member(self):
        print(222)
        sleep(5)
        self._driver.find_element(By.ID, 'username').send_keys('adbdfdfd')
        sleep(2)
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys('aaaaa')
        sleep(2)
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys('1111111111')
        sleep(5)
        self._driver.quit()
        return True