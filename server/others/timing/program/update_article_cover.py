# -*- coding: utf-8 -*-
# @Time : 2022/5/1 10:33
# @Author : kaede
# @File : update_article_cover.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
# 每天自动更新文章封面
# -*- Description -*-
import os
import random
import logging
import requests
import json

BASE_URL_ARTICLES = 'http://49.234.15.210/original/articles'  # 文章接口的基本地址
BASE_URL_COVER = 'http://49.234.15.210/static/web/articles/'  # 文章封面图片的基本地址
BASE_URL_TOKEN = "http://49.234.15.210/account/token/get"  # 获取token的API

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s',
                    filemode='a',
                    filename='/home/server/others/timing/log/update_article_cover.txt')


def get_token():
    """
    获取token
    :return: token
    """
    payload = {'username': 'Kaede',
               'password': 'Ping.1235'}
    files = [

    ]
    headers = {}

    response = requests.request("POST", BASE_URL_TOKEN, headers=headers, data=payload, files=files)
    response = json.loads(response.text)
    return response['token']


def set_url():
    """
    1.获取token信息
    2.获取服务器静态资源文件下面的图片列表
    3.循环获取到的文章
    4.循环文章数量，发送请求，修改文章封面地址
    :return:
    """

    # 获取token信息
    token = get_token()

    # 获取服务器静态资源文件下面的图片列表
    file_list = os.listdir('/home/server/others/static/web/articles')

    # 获取所有的文章列表
    response = requests.request("GET", BASE_URL_ARTICLES)
    response = json.loads(response.text)

    # 循环每篇文章
    for i in response:
        logging.info('old=>{}:{}'.format(str(i['id']), i['cover_url']))  # 输出原文章封面地址
        cover = BASE_URL_COVER + random.choice(file_list)
        put_url = BASE_URL_ARTICLES + '/' + str(i['id'])
        logging.info('new=>{}:{}'.format(str(i['id']), cover))  # 输出新封面地址
        payload = {'title': i['title'],
                   'description': i['description'],
                   'last_up_date': i['last_up_date'],
                   'cover_url': cover.replace(' ', '%20'),
                   'address': i['address']}
        files = [
        ]
        headers = {
            'Authorization': 'token ' + token
        }
        response = requests.request("PUT", put_url, data=payload, headers=headers, files=files)
        logging.info(response)


def main():
    """
    程序入口
    :return:
    """
    logging.debug('------------------------Start------------------------')
    logging.debug('Program start!')

    logging.debug('Start set_url function!')
    set_url()
    logging.debug('End set_url function!')

    logging.debug('Program end!')
    logging.debug('------------------------End------------------------')


if __name__ == '__main__':
    main()
