#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/2 16:00
# @File: main.PY
# @Software: PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_wework_main.page.add_member import AddMember


class Main:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')

    def goto_add_member(self):
        # click add member
        self._driver.find_element_by_link_text("企业登录").click()
        sleep(19)
        self._driver.find_element_by_link_text("添加成员").click()
        print(11111)
        return AddMember(self._driver)