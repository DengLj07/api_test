# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/13
@Auth ： wb.denglijiao@mesg.corp.netease.com
@Dev : 
@Doc Url :
"""
from base.base_api import BaseApi


class Questions(BaseApi):

    def __init__(self):
        super().__init__()

    def add_question(self, **kwargs):
        pyload = kwargs
        self.payload_template = self.conf['']
        pyload = self.payload_template.update
        self.env.manager_url =

