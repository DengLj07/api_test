# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/23
@Auth ： wb.denglijiao@mesg.corp.netease.com
@Dev : 
@Doc Url :
"""
import json
from sq_interface.config.config import HOST

class Login:

    def login(self, in_data, token_flag=True):
        url = f'{HOST}/account/sLogin'
        in_data = json.loads(in_data)  # 字符串转json
        print(in_data)
        pass
