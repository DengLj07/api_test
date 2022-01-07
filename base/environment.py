# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/24
@Auth ： wb.denglijiao@mesg.corp.netease.com
@Dev : 
@Doc Url :
"""


class Url:

    def __init__(self, host: str, port: int, schema: str = 'http'):
        self.host = host
        self.port = port
        self.schema = schema

    def __repr__(self):
        return f'{self.host}://{self.host}:{self.port}'


class Environment:
    """环境"""

    @property
    def manager_url(self) -> Url:
        raise NotImplementedError

    @property
    def business_url(self) -> Url:
        raise NotImplementedError

    @property
    def staging_env(self) -> Url:
        raise NotImplementedError

    @property
    def product_env(self) -> Url:
        raise NotImplementedError


class Test01Environment(Environment):
    """测试服01"""

    @property
    def manager_url(self):
        return Url('', 80)
    # 管理后台地址


class Test03Environment(Environment):
    """测试服03"""

    @property
    def manager_url(self):
        return Url('', 80)


class StagingEnvironment(Environment):
    """预发服"""

    @property
    def manager_url(self):
        return Url('', 80)


def make_env(env_str: str = 'test01') -> Environment:

    if env_str == 'test01':
        return Test01Environment()
    if env_str == 'test03':
        return Test03Environment()
    if env_str == 'staging':
        return StagingEnvironment()

    raise Exception(f'env_str error:{env_str}')

