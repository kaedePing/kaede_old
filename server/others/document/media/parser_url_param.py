# -*- coding: utf-8 -*-
# @Time : 2023/1/5 16:08
# @Author : kaede
# @File : parser_url_param.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
#
#
# -*- Description -*-
import json


def parser(text):
    """
    传入url地址，解析出地址后面携带的参数，即?后面的每个参数
    :param text: url地址
    :return: 返回解析后的参数json数据
    """
    result = {}
    temp = text[text.find('?') + 1:]
    while temp:
        index = temp.find('=')
        key = temp[:index]
        temp = temp[index + 1:]
        index = temp.find('&')

        if index == -1:
            value = temp
            temp = ''
        else:
            value = temp[:index]
            temp = temp[index + 1:]
        result[key] = value
    return result


if __name__ == '__main__':
    url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1672904874789&mid=c9c0c7525f0c171140718e82b6c79816&uuid=c9c0c7525f0c171140718e82b6c79816&dfid=1txqNy31Q9Q23UXTFP4aZhNo&keyword=letting+go&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=212d2149e23fc63d2c7ed9e956761e3c'

    url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1672970019704&mid=c9c0c7525f0c171140718e82b6c79816&uuid=c9c0c7525f0c171140718e82b6c79816&dfid=1txqNy31Q9Q23UXTFP4aZhNo&keyword=Not+Angry&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=52f06433e443bd0e4e94003d86dffb72'

    url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&mid=1&encode_album_audio_id=44ec85c4'

    url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1676514981865&mid=594c6049da0bb464094022e291c17d24&uuid=594c6049da0bb464094022e291c17d24&dfid=1txkzd2KhWHC0r2aHv0rFzXP&keyword=%E8%B0%AA%E4%BB%99&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=71ab94156a117546ad6d88532564b94d'

    print(parser(url))
