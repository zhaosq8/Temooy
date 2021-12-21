#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/20 16:19
# @File: add_member.PY
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import main


class AddMember:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_member(self):
        # sendkeys
        sleep(5)
        self._driver.find_element(By.ID, 'username').send_keys("abcdeffff")
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys("adbvcddff")
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys("11111111111")
        self._driver.find_element(By.CSS_SELECTOR, '.qui_btn ww_btn js_btn_save').click()
        sleep(8)
        self._driver.quit()
        return True


a = AddMember()
a.add_member()