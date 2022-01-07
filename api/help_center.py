# -*- coding: utf-8 -*-
"""

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

