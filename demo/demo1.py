#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/15 16:33
# @File: demo1.PY
# @Software: PyCharm
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(5)