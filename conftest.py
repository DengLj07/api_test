# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/24
@Auth ： wb.denglijiao@mesg.corp.netease.com
@Dev : 
@Doc Url :
"""
import os
import pytest

from base.environment import make_env


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="test03", help="要连接的测试环境，如: test01, test03"
    )


@pytest.fixture(scope='session', autouse=True)
def env(request):
    env_str = request.config.getoption('--env')
    os.environ['env_str'] = env_str  # 加入系统环境中去，子类可以去系统环境中读取url
