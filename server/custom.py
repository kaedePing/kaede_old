# -*- coding: utf-8 -*-
# @Time : 2023/3/30 16:39
# @Author : kaede
# @File : custom.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
# 自定义如下类，用来存储，方便服务器其他资源访问
# 1.Constant 存储常量
# -*- Description -*-
import os


class Constant:
    host = '49.234.15.210'  # ip地址
    settings_debug = True if (os.name == 'nt') else False  # django的settings文件中是否调试模式
