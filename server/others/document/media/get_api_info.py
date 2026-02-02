# -*- coding: utf-8 -*-
# @Time : 2023/3/2 10:10
# @Author : kaede
# @File : get_api_info.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
# 通过request解析出ip等信息，并存入数据库中
# -*- Description -*-
import requests
from bs4 import BeautifulSoup
import logging
import os

LOG_NAME = os.getcwd() + '/others/common/log/get_ip_info.txt'  # 日志存放位置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s',
                    filemode='a',
                    filename=LOG_NAME)


def save_info(data):
    """
    将通过request解析出来的信息存入服务器中
    :param data:
    :return:
    """
    url = ''
    response = requests.request("POST", url, data=data)
    logging.debug('upload results:' + response.text)


def main(request=None):
    """
    传入request解析ip等信息
    :param request:
    :return: 提取的信息
    """
    logging.info('------------------------Start------------------------')
    logging.info('Program start!')

    if not request:
        return None
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    param = request.META.get('QUERY_STRING')
    path = request.META.get('PATH_INFO')
    method = request.method
    if method == 'GET':
        get_or_post_param = request.GET
    elif method == 'POST':
        get_or_post_param = request.POST
    else:
        get_or_post_param = None

    url = 'https://zh-hans.ipshu.com/ipv4/' + ip
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    detail = soup.select(
        'body>div.main>section.content.p-sm.gray_bg>div>div>div.col.left_side>div.region.region-content>div:nth-child(1)>div>img')
    info = detail[0].select('td')
    continent = info[3].text.strip()  # 大洲
    country_code = info[5].text.replace('?', '').strip()  # 国家或地区代码
    country_name = info[7].text.replace('?', '').strip()  # 国家或地区名称
    area_name = info[9].text.strip()  # 地区名称
    city_name = info[11].text.strip()  # 城市名称
    city_latitude = info[13].text.strip()  # 城市纬度
    city_longitude = info[15].text.strip()  # 城市经度
    more = soup.select(
        'body>div.main>section.content.p-sm.gray_bg>div>div>div.col.left_side>div.region.region-content>div:nth-child(3)>div>div>div:nth-child(1)')
    service_provider = more[0].select('td')[1].text
    result = {
        'method': method,
        'path': path,
        'query_string': param,
        'get_or_post_param': get_or_post_param,
        'ip': ip,
        'continent': continent,
        'country_code': country_code,
        'country_name': country_name,
        'area_name': area_name,
        'city_name': city_name,
        'city_latitude': city_latitude,
        'city_longitude': city_longitude,
        'service_provider': service_provider
    }

    logging.info('Start save_info function!')

    logging.info('End save_info function!')
    save_info(result)
    logging.info('Program end!')

    return result


if __name__ == '__main__':
    pass
