# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/24
@Auth ： wb.denglijiao@mesg.corp.netease.com
@Dev : 
@Doc Url :
"""
import allure
import pytest


# 定义测试类标签，login
@pytest.mark.login
@allure.epic('松勤项目')
@allure.feature('登录模块')
class TestLogin:

    def setup_class(self):
        print('---测试类----')

    @allure.story('登录')
    @allure.title('登录用例')
    @pytest.mark.test_01
    @pytest.mark.usefixtures('my_fixture')  # my_fixture 不能有返回值
    @pytest.mark.parametrize('uid', ['wda'])
    @pytest.mark.parametrize('psw', ['123'])  # psw先执行，靠近函数的优先执行
    def test_01(self):
        print('测试用例一')

    @pytest.mark.test_02  # 标签
    def test_02(self):
        print('测试用例二')
