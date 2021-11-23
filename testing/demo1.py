#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:zhaosq
# @Time: 2021/11/18 11:22
# @File: demo1.py.PY
# @Software: PyCharm
import pytest
import pytest_assume


class TestDemo(object):
    # def setup(self):
    #     print('setup')
    #
    # def teardown(self):
    #     print('teardown')

    # def test_one(self,login):
    #     print("开始执行， test_one方法")
    #     x = 'this'
    #     assert 'h' in x
    #
    # def test_two(self):
    #     print("开始执行， test_two方法")
    #     x = 'help'
    #     assert 'e' in x
    #
    # def test_three(self):
    #     a = 'hello'
    #     b = 'hello world'
    #     pytest_assume(a in b)
    #     pytest_assume('e' in a)
    #     pytest_assume('p' in a)

    @pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+5", 7), ("7*5", 30)])
    def test_evel(self, test_input, expected):
        assert eval(test_input) == expected


if __name__=='__main__':
    pytest.main("-v -x -s TestDemo")