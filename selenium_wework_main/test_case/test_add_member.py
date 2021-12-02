#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/12/2 16:29
# @File: test_add_member.PY
# @Software: PyCharm
from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        self.main.goto_add_member().add_member()
