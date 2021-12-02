#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/11/24 14:54
# @File: test_wait.PY
# @Software: PyCharm
from time import sleep

import pytest
from selenium import webdriver


class TestWait(object):

    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://home.testing-studio.com/')

    def test_wait(self):
        sleep(3)
        print('hello')
