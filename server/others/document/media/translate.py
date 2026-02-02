# -*- coding: utf-8 -*-
# @Time : 2022/11/23 16:50
# @Author : kaede
# @File : translate.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
# 解密有道云翻译，模拟其翻译Ajax请求
# -*- Description -*-
import json
import time
import hashlib
import requests

url='https://fanyi.youdao.com/index.html#/'

RELATION = {
    '自动': 'AUTO',
    '中文': 'zh-CHS',
    '英语': 'en',
    '日语': 'ja',
    '韩语': 'ko',
    '法语': 'fr',
    '德语': 'de',
    '俄语': 'ru',
    '西班牙语': 'es',
    '葡萄牙语': 'pt',
    '意大利语': 'it',
    '越南语': 'vi',
    '印尼语': 'id',
    '阿拉伯语': 'ar',
    '荷兰语': 'n1',
    '泰语': 'th'
}


def get_param(word='枫叶'):
    """
    获取请求需要的表单数据 salt sign
    salt:取前系统的时间戳13位再加一位随机数 可以默认取时间戳14位
    sign:一段字符的md5加密
    :param word:需要翻译的单词
    :return:salt sign
    """
    salt = str(time.time()).replace('.', '')[:14]
    sign_str = "fanyideskweb" + word + salt + "Ygy_4c=r#e#4EX^NUGUc5"
    sign = hashlib.md5(sign_str.encode()).hexdigest()

    return salt, sign


def parse_response(code, response):
    """
    解析返回的结果，提取对应的字段
    :param code: 请求的返回状态码
    :param response: 请求的返回结果
    :return: 提取的翻译结果，list类型，嵌套字典
    """
    print(response)
    result = []
    if code == 200:
        data = json.loads(response)
        try:
            for i in data['translateResult'][0]:
                source = i['src']
                target = i['tgt']
                result.append({
                    'source': source,
                    'target': target
                })
        except Exception as e:
            return e
        return result
    return


def get_headers():
    """
    模拟其网页翻译请求时，需要固定的headers信息，通过此函数获取拼装好的headers
    :return: 返回网页请求的header信息
    """
    cookie = "OUTFOX_SEARCH_USER_ID=-1506602845@10.169.0.82; JSESSIONID=aaaUggpd8kfhja1AIJYpx; OUTFOX_SEARCH_USER_ID_NCOO=108436537.92676207; ___rl__test__cookies=1597502296408"
    headers = {
        "Cookie": cookie,
        "Referer": "http://fanyi.youdao.com/",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    return headers


def get_data(word='枫叶', source='自动', target='自动'):
    """
    获取请求的表单数据
    :param word: 需要翻译的单词
    :param source: 原单词语言
    :param target: 目标语言
    :return: 目标语言的翻译结果
    """
    salt, sign = get_param(word)
    data = {
        'i': word,
        'from': RELATION[source],
        'to': RELATION[target],
        'smartresult': 'dict',
        'client': 'fanyideskweb',

        'salt': salt,
        'sign': sign,

        'bv': '9edd1e630b7d8f13679a536d504f3d9f',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    return data


def translate(word='枫叶', source='自动', target='自动'):
    """
    传入需要翻译的词，以及源语言和目标语言，返回翻译结果
    注意:可以不指明语言，自动识别
    :param word: 需要翻译的单词
    :param source: 原单词语言
    :param target: 目标语言
    :return: 目标语言的翻译结果
    """
    if source not in RELATION:
        source = '自动'
    if target not in RELATION:
        target = '自动'
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = get_headers()
    data = get_data(word, source, target)
    res = requests.post(url=url, headers=headers, data=data)
    return parse_response(res.status_code, res.text)


if __name__ == '__main__':
    origin_word = '紅葉'
    source_language = '日语'
    target_language = '英语'
    print(translate(origin_word, source_language, target_language))
