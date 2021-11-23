#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Authon:zhaosq
# @Time: 2021/11/23 16:04
# @File: conftest.PY
# @Software: PyCharm
import pytest


@pytest.fixture()
def login():
    print("这是登陆方法")


# 把标签放到同一个地方，运行就不回提示错误
def pytest_configure(config):
    marker_list = ["search", "login"]
    for markers in marker_list:
        cofig.addinivalue_list(
            "markers", markers
        )