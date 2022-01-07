# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/11
@Auth ： wb.denglijiao@mesg.corp.netease.com
@Dev : 
@Doc Url :
"""
from pprint import pprint

import yaml


class Config:

    @classmethod
    def read_yaml(cls, path) -> dict:
        with open(path, 'r', encoding='utf8') as f:
            content = yaml.safe_load(f.read())
        return content

    @classmethod
    def write_yaml(cls, path, data):
        with open(path, 'w', encoding='utf8') as f:
            yaml.safe_dump(data, f)


if __name__ == '__main__':
    print(__file__)
    data = Config.read_yaml('../../data/question_data.yaml')
    pprint(data)