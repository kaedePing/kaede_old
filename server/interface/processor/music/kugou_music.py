# # -*- coding: utf-8 -*-
# # @Time : 2023/1/5 16:05
# # @Author : kaede
# # @File : kugou_music.py
# # @Software: PyCharm
# # @contact: flowerslanguage@126.com
# # -*- Description -*-
# # 传入歌曲名、歌手名两个参数去搜索下载指定的歌曲内容。
# # 下载包括mp3源文件、歌词信息
# # 如果找不到指定歌曲，则取特定的第几条作为返回结果。
# # -*- Description -*-
# import json
#
# import requests
# import os
# import logging
# import execjs  # pip install PyExcelJS  # sudo apt-get install nodejs
#
# PATH = os.getcwd() + '/interface/processor/music/file'  # mp3存放路径
# LOG_NAME = os.getcwd() + '/others/common/log/interface.txt'  # 日志存放位置
# WHICH_NUMBER = 0  # 当输入的参数匹配不到搜索结果的任何东西时，取第几条数据作为返回结果
# JS_FILE = os.getcwd() + '/interface/processor/music/get_signature.js'  # js加密的路径
# BASE_MUSIC_URL = 'http://49.234.15.210/music/v1s'  # music接口的基本地址
# BASE_PLAY_URL = 'http://49.234.15.210/api/music/v1/play'  # 歌曲播放地址
# BASE_DOWNLOAD_URL = 'http://49.234.15.210/api/music/v1/download'  # 歌曲下载地址
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s',
#                     filemode='a',
#                     filename=LOG_NAME)
#
#
# def mock_ajax_request(sing_title):
#     """
#     根据参数歌曲名去模拟搜索的Ajax请求,分为两步
#     1.获取signature
#     2.构造Ajax参数
#     :param sing_title:
#     :return:
#     """
#     client_time = '1676514981865'
#     mid = uuid = '594c6049da0bb464094022e291c17d24'
#     d_fid = '1txkzd2KhWHC0r2aHv0rFzXP'
#
#     # 获取signature前需要加密的参数
#     param = ['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
#              'appid=1014',
#              'bitrate=0',
#              'callback=callback123',
#              'clienttime=' + client_time,
#              'clientver=1000',
#              'dfid=' + d_fid,
#              'filter=10',
#              'inputtype=0',
#              'iscorrection=1',
#              'isfuzzy=0',
#              'keyword=' + sing_title,
#              'mid=' + mid,
#              'page=1',
#              'pagesize=30',
#              'platform=WebFilter',
#              'privilege_filter=0',
#              'srcappid=2919',
#              'token=',
#              'userid=0',
#              'uuid=' + uuid,
#              'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
#     # 获取signature
#     with open(JS_FILE, 'r') as f:
#         read = f.read()
#         js = execjs.compile(read)
#         signature = js.call('main', ''.join(param))
#     logging.info('signature:' + signature + '!')
#     # 构造Ajax请求的参数获取对应歌曲的搜索内容
#     url = "https://complexsearch.kugou.com/v2/search/song"
#     params = dict(callback='callback123',
#                   srcappid='2919',
#                   clientver='1000',
#                   clienttime=client_time,
#                   mid=mid,
#                   uuid=uuid,
#                   dfid=d_fid,
#                   keyword=sing_title,
#                   page='1',
#                   pagesize='30',
#                   bitrate='0',
#                   isfuzzy='0',
#                   inputtype='0',
#                   platform='WebFilter',
#                   userid='0',
#                   iscorrection='1',
#                   privilege_filter='0',
#                   filter='10',
#                   token='',
#                   appid='1014',
#                   signature=signature)
#     res = requests.get(url, params=params)
#     return res.text
#
#
# def analysis(response, sing_title, singer):
#     """
#     根据搜索返回的结果 歌曲名 歌手名提取到指定的EMixSongID,返回
#     注: response前面有一个字符串 callback123,以及伴随着有一个(),需要处理掉才能转换成对应的标准格式
#     1.首先根据参数找到特定的歌曲(需要对参数做格式化，去掉空格、全都变成小写)
#     2.如果第一步找不到，则取返回结果的第一条数据
#     :param response: 模拟搜索的Ajax请求结果
#     :param sing_title: 歌曲名
#     :param singer: 歌手
#     :return: 对应一个歌曲的 EMixSongID=>song_number
#     """
#     song_number = ''
#     response = response.strip()
#     response = response.lstrip('callback123').lstrip('(').rstrip(')')
#     response_data = json.loads(response)
#     data_list = response_data['data']['lists']
#     format_singer = singer.replace(' ', '').lower()
#     format_sing_title = sing_title.replace(' ', '').lower()
#     for i in data_list:
#         if i['SingerName'].replace(' ', '').lower() == format_singer \
#                 and i['SongName'].replace(' ', '').lower() == format_sing_title:
#             song_number = i['EMixSongID']
#             break
#     # 如果根据输入的参数找不到指定的歌曲，则取第一条数据
#     if not song_number:
#         song_number = data_list[WHICH_NUMBER]['EMixSongID']
#     return song_number
#
#
# def get_detailed_information(songNumber):
#     """
#     传入对应歌曲的EMixSongID，模拟获取歌曲详细信息的请求，解析对应的数据
#     注：需要注意返回的字符串中有一种字符true、false需要做一下处理，替换成对应的字符串，即加一个双引号
#     :param songNumber: 对应的 EMixSongID
#     :return: 对应歌曲的详细信息
#     """
#     detail_url = 'https://wwwapi.kugou.com/yy/index.php'
#     detail_info_params = {
#         'r': 'play/getdata',
#         'mid': '1',
#         'encode_album_audio_id': songNumber
#     }
#     res = requests.get(detail_url, params=detail_info_params)
#     response_data = res.text.replace('true', '"true"').replace('false', '"false"')
#     response_data = json.loads(response_data)
#     data = {}
#     try:
#         data['audio_name'] = response_data['data']['audio_name']
#         data['author_name'] = response_data['data']['author_name']
#         data['song_name'] = response_data['data']['song_name']
#         data['lyrics'] = response_data['data']['lyrics']
#         data['play_url'] = response_data['data']['play_url']
#     except Exception as e:
#         logging.error(e)
#     finally:
#         logging.debug('Detail data:')
#         logging.info(data)
#         return data
#
#
# def create_folder(path):
#     """
#     判断该路径下的文件夹是否存在，存在则返回True;不存在则创建成功后返回True,
#     :param path:
#     :return:
#     """
#     if not os.path.exists(path):
#         os.mkdir(path)
#     return os.path.exists(path)
#
#
# def download(path, play_url, music_name):
#     """
#     传入播放地址下载对应的源文件
#     :param path: 存放路径
#     :param play_url: 播放地址
#     :param music_name: 保存的音乐名
#     :return:
#     """
#     if create_folder(path):
#         res = requests.get(play_url)
#         with open(path + '/' + music_name + '.mp3', 'wb') as f:
#             f.write(res.content)
#     else:
#         logging.error('下载失败!')
#
#
# def post_info_to_interface(sing_title, singer, play_url, music_name):
#     """
#     将下载歌曲后的其他信息放入服务器的对应接口中
#     :param sing_title: 歌名
#     :param singer: 歌手
#     :param play_url: 原网站播放地址
#     :param music_name: 音乐名
#     :return:
#     """
#     payload = {
#         'flag': 'Y',
#         'sing_title': sing_title,
#         'singer': singer,
#         'name': music_name + '.mp3',
#         'playLink': BASE_PLAY_URL,
#         'downloadUrl': BASE_DOWNLOAD_URL,
#         'originDownloadUrl': play_url
#     }
#     response = requests.request("POST", BASE_MUSIC_URL, data=payload)
#     logging.info('upload result:' + response.text)
#
#
# def main(sing_title, singer):
#     """
#     主函数，流程包括接收歌曲名和歌手获取对应的下载链接，然后下载返回给对方
#     1.首先根据歌曲名去模拟Ajax请求，获取到返回结果
#     2.从返回结果中提取到类似的歌手，找到对应的 EMixSongID
#     3.根据 EMixSongID去获取到对应歌曲的详细信息，包括比如mp3地址、歌词信息等
#     4.调用download下载对应的源文件
#     5.将对应的歌曲信息放入服务器中
#     :param sing_title: 歌名
#     :param singer: 歌手
#     :return:
#     """
#     logging.debug('------------------------Start------------------------')
#     logging.debug('Program start!')
#     logging.debug('Here are the input parameters:')
#     logging.info('sing_title:' + sing_title)
#     logging.info('singer:' + singer)
#
#     try:
#         # 1.模拟搜索歌曲的Ajax请求，获取到返回结果
#         logging.debug('Start mock_ajax_request function!')
#         response = mock_ajax_request(sing_title)
#         logging.debug('End mock_ajax_request function!')
#
#         # 2.根据搜索结果+参数提取到指定的歌曲EMixSongID=>song_number
#         logging.debug('Start analysis function!')
#         song_number = analysis(response, sing_title, singer)
#         logging.debug('End analysis function!')
#
#         # 3.传入对应的EMixSongID获取歌曲的详细信息
#         logging.debug('Start get_detailed_information function!')
#         detail_data = get_detailed_information(song_number)
#         logging.debug('End get_detailed_information function!')
#
#         # 4.下载对应的音乐
#         play_url = detail_data['play_url']
#         music_name = detail_data['audio_name']
#         logging.debug('Start download function!')
#         download(PATH, play_url, music_name)
#         logging.debug('End download function!')
#
#         # 5.将对应的歌曲信息放入服务器中
#         logging.debug('Start post_info_to_interface function!')
#         post_info_to_interface(sing_title, singer, play_url, music_name)
#         logging.debug('End post_info_to_interface function!')
#
#     except Exception as e:
#         logging.error(e)
#
#     logging.debug('Program end!')
#     logging.debug('------------------------End------------------------')
#
#
# if __name__ == '__main__':
#     param1 = '富士山下'
#     param2 = '叶 里'
#     main(param1, param2)
