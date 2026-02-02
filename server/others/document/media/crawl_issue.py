# -*- coding: utf-8 -*-
# @Time : 2022/11/3 17:09
# @Author : kaede
# @File : crawl_issue.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
# 获取AcFun上的投稿视频信息
#
# -*- Description -*-
import time
import traceback
import requests
from pyquery import PyQuery
import pandas as pd
import pymongo
import logging

LOG_NAME = '../log/video.txt'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s',
                    filemode='a',
                    filename=LOG_NAME)


def structure_url(page=10):
    """
    构造需要爬取的网页地址
    :param page: 需要爬取的网页页数
    :return: 返回需要爬取的网页连接
    """
    urls = []
    for index in range(1, page + 1):
        urls.append(
            'https://www.acfun.cn/v/list159/index.htm?sortField=createTime&duration=all&date=default&page={}'.format(
                str(index)))
    return urls


def parse_message(url):
    """
    1.请求网页
    2.解析返回内容，提取到只包含一个投稿视频的整体标签div
    3.从每个整体div标签里提取到需要的信息 up 标题 时常 播放数量 评论数量 封面地址
    :param url: 需要请求的地址
    :return: 最终提取的解析内容
    """
    logging.debug('开始获取 ' + url + ' 网页信息！')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    try:
        request = requests.get(url, headers=headers)
        doc = PyQuery(request.text)
        items = doc.find('.list-content-item')
        results = []
        for i in items.items():
            up = i.find('.list-content-uplink').text()
            title = i.find('.list-content-title').text()
            often = i.find('.video-time').text()
            view_count = i.find('.viewCount').text()
            comment_count = i.find('.commentCount').text()
            view_url = 'https://www.acfun.cn' + i.find('.list-content-top').attr('href')
            img = i.find('img').attr('src')

            result = {
                'up': up,
                'title': title,
                'often': often,
                'view_count': view_count,
                'comment_count': comment_count,
                'view_url': view_url,
                'img': img
            }
            results.append(result)
        logging.debug('获取 ' + url + ' 网页信息成功！')
        return results
    except Exception as e:
        logging.error('获取 ' + url + ' 网页信息失败！')
        logging.error(e)
        logging.error(traceback.format_exc())
        # logging.error(traceback.format_exception(e))
        return None


def download_file(stream):
    """
    将获取的视频相关信息下载到本地csv
    :param stream:list类型，嵌套dict，每个dict包含视频的相关信息
    :return:
    """
    logging.debug('开始下载信息到csv！')
    csv_name = '../file/' + time.strftime('%Y-%m-%d %H-%M-%S ') + 'video' + '.csv'
    df = pd.DataFrame(stream)
    head = ['up🐖', '标题', '时长', '播放量', '评论数', '视频地址', '封面地址']
    try:
        df.to_csv(csv_name, index=False, header=head, encoding='utf_8_sig')
        logging.debug('下载信息到csv成功！')
    except Exception as e:
        logging.error('下载信息到csv失败！')
        logging.error(e)
        logging.error(traceback.format_exc())
        # logging.error(traceback.format_exception(e))


def insert_db(stream):
    """
    将获取的视频相关信息存入到数据库中
    :param stream:
    :return: list类型，嵌套dict，每个dict包含视频的相关信息
    """
    logging.debug('开始将下载信息插入到数据库中！')
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client.kaede
        collection = db.video
        result = collection.insert_many(stream)
        logging.debug('将下载信息插入到数据库中成功！')
        logging.info(result)
    except Exception as e:
        logging.debug('将下载信息插入到数据库中失败！')
        logging.error(e)
        logging.error(traceback.format_exc())
        # logging.error(traceback.format_exception(e))


if __name__ == '__main__':
    logging.info('start program！')
    videos = []

    logging.info('start parse_message！')
    for x in map(parse_message, structure_url(10)):
        for y in x:
            videos.append(y)
    logging.info('end parse_message！')

    logging.info('start download_file！')
    download_file(videos)
    logging.info('end download_file！')

    logging.info('start insert_db！')
    insert_db(videos)
    logging.info('end insert_db！')

    logging.info('end program！')
