# -*- coding: utf-8 -*-
# @Time : 2022/6/21 11:13
# @Author : kaede
# @File : get_token.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
# 该文件专门用来获取Django管理员的token，用来判断客户端是否允许对某些数据进行操作
# -*- Description -*-
import requests
import json


def get_token():
    """
    获取token
    :return: token
    """
    url = "http://49.234.15.210/account/token/get"  # 获取token的API
    payload = {'username': 'Kaede',
               'password': 'Ping.1235'}
    files = [

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response = json.loads(response.text)
    return response['token']


if __name__ == '__main__':
    get_token()
