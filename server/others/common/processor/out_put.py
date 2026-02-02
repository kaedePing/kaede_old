# -*- coding: utf-8 -*-
# @Time : 2023/3/30 14:58
# @Author : kaede
# @File : out_put.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
# 用于格式化输出日志，根据调试模式还是非调试模式来控制输出的方式
# print:调试模式 logging:非调试模式
# -*- Description -*-
import logging
from django.conf import settings


def put(text, logging_type=logging.DEBUG):
    """
    根据配置文件的调试模式、非调试模式来动态输出信息
    :param text: 需要输出的内容
    :param logging_type: logging的等级，分三种。logging.DEBUG、logging.INFO、logging.ERROR
    :return:
    """
    if settings.DEBUG is True:
        print(text)
    else:
        if logging_type == logging.DEBUG:
            logging.debug(text)
        elif logging_type == logging.INFO:
            logging.info(text)
        elif logging_type == logging.ERROR:
            logging.error(text)
        else:
            print(text)


if __name__ == '__main__':
    pass
