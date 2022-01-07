# -*- coding: utf-8 -*-
"""

"""
import logging
import datetime
# 对日志设置
import os

"""
1.存放路径
2.日志文件名
3.内容格式 2021_10_31 12:00:00-logbasic.py [代码错误的行号] 级别：具体内容
"""
def logger():
    # 调用配置函数
    logging.basicConfig(
        format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s : %(message)s',
        filename=f"../logs/{datetime.datetime.now().strftime('%Y-%m-%d')}.log",
        level=logging.INFO,
        filemode='a',

    )
    return logging



if __name__ == '__main__':
    logger().info('---hello--打算')

