# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/24
@Auth ： wb.denglijiao@mesg.corp.netease.com
@Dev : 
@Doc Url :
"""
import yaml


def get_yaml_data(file_path):
    """
    读取yaml文件
    :param file_path:
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)

    return yaml_data

def get_yaml_data2(file_path):
    """
     yaml以 --- 分割为多个时
    :param file_path:
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        yaml_data = yaml.load_all(f, Loader=yaml.FullLoader)

        for one in yaml_data: # yaml以 --- 分割为多个时
            print(one)
        return yaml_data

if __name__ == '__main__':
    data = get_yaml_data2('../data/conf.yaml')

    # print(data)
