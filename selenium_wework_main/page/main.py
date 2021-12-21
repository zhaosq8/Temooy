#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/20 15:55
# @File: main.PY
# @Software: PyCharm
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_wework_main.page.add_member import AddMember


class Main:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        # sleep(25)
        db = shelve.open("cookies")
        # db['cookie'] = self._driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            print("1111111111111111111111111111111111111111111111111111")
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            print("2222222222222222222222222222222222222222222222222222")
            self._driver.add_cookie(cookie)
        print("333333333333333333333333333333333333333333333333333333333")
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')

    def goto_add_member(self):
        # click add member
        self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()
        return AddMember(self._driver)
        # sleep(8)
        # self._driver.quit()


