# -*- coding: utf-8 -*-
"""

"""

import pytest


@pytest.fixture(scope='module')
def start_testcases(request):
    print('------开始执行自动化测试--------')


    def fin():
        # 作数据清除操作
        print('-------自动化测试结束-------')
    request.addfinalizer(fin)

@pytest.fixture(scope='class')
def my_fixture():
    print('----')
