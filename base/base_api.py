# -*- coding: utf-8 -*-

import os
import json as complexjson
import requests

from config.config import user
from lib.apiLib.pulgins import Config
from base.environment import Environment, make_env


class BaseApi:

    def __init__(self, cookies=None, timeout=10, verify=False):
        if cookies is None:
            '生成cookie的方法'
            self.cookies = User().login()  # 登录获取cookies
        self.cookies = cookies

        # 根据所选择的测试环境，实例测试环境
        if self
        self.env = make_env(self.env_str)
        # 超时时间
        self.timeout = timeout
        # ssl验证
        self.verify = verify
        # 接口请求参数模版
        self.conf = Config.read_yaml('file_path')[self.__class__.__name__]

    def create_env(self):
        # 从系统环境中读取测试环境url，由jenkins运行时，所选择的命令行参数决定
        try:
            env_str = os.environ['env_str']
        except KeyError:
            print('获取系统环境变量中的envstr失败')  # 日志记录

    def request(self, url, method, **kwargs):
        if method == "GET":
            return self.get(url, **kwargs)
        if method == "POST":
            return self.post(url, **kwargs)
        # if method == "PUT":
        #     if json:
        #         # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
        #         data = complexjson.dumps(json)
        #     return requests.put(url, data, **kwargs)
        # if method == "DELETE":
        #     return requests.delete(url, **kwargs)
        # if method == "PATCH":
        #     if json:
        #         data = complexjson.dumps(json)
        #     return requests.patch(url, data, **kwargs)

    # POST
    def post(self, url, **kwargs):
        """封装post方法"""
        try:
            return requests.post(url, **kwargs)
        except Exception as e:
            print(e)  # 记录日志
            return None

    # GET
    def get(self, url, **kwargs):
        """封装get方法"""
        try:
            return requests.get(url, **kwargs)
        except Exception as e:
            print(e)
            return None


class User:

    def __init__(self, user_name=None, psw=None):
        if user_name:
            self.user_name = user_name
        else:
            self.user_name = user['user_name']
        if psw:
            self.psw = psw
        else:
            self.psw = user['psw']

    def login(self):
        env = os.environ['env']
        # requests请求，进行登录，返回登录成功后的cookies
        cookies = requests.post(env) # 登录请求url
        return cookies

    def logout(self):
        pass


class Version(BaseApi):

    def __init__(self):
        super().__init__()
        self.url = None

    def add_version(self, data):
        self.url = self.conf['add_version']['url']
        method = self.conf['add_version']['method']
        payload = self.conf['add_version']['in_body']
        payload.update(data)
        self.request(self.url, method, payload)
