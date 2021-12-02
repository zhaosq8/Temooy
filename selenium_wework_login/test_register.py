#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/2 15:35
# @File: test_register.PY
# @Software: PyCharm
from selenium_wework_login.index import Index


class TestRegister:

    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_login().goto_register().register()
        # self.index.goto_register()