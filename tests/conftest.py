# coding=utf-8
"""
File: conftest.py
Created on 2023/1/16 15:54
__author__= yangh
__remark__=
"""

import pytest



pytest_plugins = ['pytester']


# @pytest.fixture()
# def login():
#     print("前置操作：准备数据")
#     assert 1 == 1  # 前置出现异常
#     yield
#     print("后置操作：清理数据")
