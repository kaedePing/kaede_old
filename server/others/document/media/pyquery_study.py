# -*- coding: utf-8 -*-
# @Time : 2022/10/29 9:33
# @Author : kaede
# @File : pyquery_study.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
#
#
# -*- Description -*-
import requests
from pyquery import PyQuery as pq


def get_request():
    url = 'https://www.acfun.cn/v/list159/index.htm?sortField=createTime&duration=all&date=default'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    text = res.text
    with open('html.txt', 'a', encoding='utf-8') as f:
        f.write(text)
    doc = pq(text)
    # print(doc('#listwrapper .list-wrapper div'))
    items = doc('#listwrapper .list-wrapper div')
    a = items.find('a')
    for item in a.items():
        print(item.attr.href)
        print(item.text())
        print(item.html())


if __name__ == '__main__':
    get_request()
