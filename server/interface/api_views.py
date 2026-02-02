import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import os
import sys
from interface.models import MusicKuGou
from django.http import HttpResponse, Http404, QueryDict
from django.http import StreamingHttpResponse, FileResponse
from django.utils.encoding import escape_uri_path  # 解决中文不能下载的问题
from others.common.processor import get_api_info
from interface.processor.music import kugou_music as music_v1
from interface.processor import translate as ts

ERROR_PAGE = os.getcwd() + '/others/static/404.html'


# 解决Django设置的django.middleware.csrf.CsrfViewMiddleware 防止跨站请求伪造的功能
# 加上下面的注解表示该函数不需要CSRF验证
@csrf_exempt
def translate(request):
    """
    翻译前端传入的关键字段，分两种请求类型。GET or Post
    分别通过对应的类型(GET/POST)获取参数，类型是键值对，
    一个键包含一个list，因此后面做参数传递时需要注意
    关于request的参数可以参考 :
    https://blog.csdn.net/qq_17584941/article/details/123865968
    :param request:
    :return: 对应翻译结果的json
    """

    get_api_info.main(request)

    if request.method == 'GET':
        temp = request.GET
    elif request.method == 'POST':
        temp = request.POST
    else:
        return HttpResponse('错误的请求类型！')

    data = dict(temp)
    if not data or 'origin_word' not in data or not data['origin_word']:
        return HttpResponse('缺少参数origin_word！')
    else:
        origin_word = data['origin_word'][0]
        try:
            source_language = data['source_language'][0]
            target_language = data['target_language'][0]
            return HttpResponse(ts.translate(origin_word, source_language, target_language))
        except:
            return HttpResponse(ts.translate(origin_word))


def search_music_v1(request):
    """
    根据前端传入的参数搜索对应的歌曲，返回特定的歌曲id
    :param request:
    :return:
    """
    get_api_info.main(request)

    if request.method == 'GET':
        temp = request.GET
    elif request.method == 'POST':
        temp = request.POST
    else:
        return HttpResponse('错误的请求类型！')
    data = dict(temp)
    if not data or 'sing_title' not in data or 'singer' not in data:
        return HttpResponse('参数不正确！')
    param1 = data['sing_title'][0]
    param2 = data['singer'][0]
    if param1 is None or param2 is None:
        return HttpResponse('参数不能为空！')

    # 格式化参数，查找表里是否存在该信息
    sing_title = param1.lower().replace(' ', '').strip()
    singer = param2.lower().replace(' ', '').strip()
    data = MusicKuGou.objects.filter(format_sing_title=sing_title, format_singer=singer)

    # 存在则返回播放地址
    if data:
        return HttpResponse(data[0].id)
    # 不存在则下载歌曲
    music_v1.main(param1, param2)

    # 再搜索对应的信息返回播放地址
    data = MusicKuGou.objects.filter(format_sing_title=sing_title, format_singer=singer)
    if data:
        return HttpResponse(data[0].id)

    # 如果搜索不到内容，则返回错误页面
    try:
        with open(ERROR_PAGE, 'r') as f:
            temp = f.read()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse(temp)


def get_music_v1_play(request, pk):
    """
    返回该歌曲id的源文件地址 播放
    :param request:
    :param pk:
    :return:
    """
    get_api_info.main(request)

    data = MusicKuGou.objects.filter(id=pk)
    if data:
        file = open(os.getcwd() + '/interface/processor/music/file/' + data[0].name, 'rb').read()
        return HttpResponse(file, content_type='audio/mpeg')
    try:
        with open(ERROR_PAGE, 'r') as f:
            temp = f.read()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse(temp)


def get_music_v1_download(request, pk):
    """
    返回该歌曲id的源文件 下载
    :param request:
    :param pk:
    :return:
    """
    get_api_info.main(request)

    try:
        data = MusicKuGou.objects.filter(id=pk)
        url = os.getcwd() + '/interface/processor/music/file/' + str(data[0].name)
        r = StreamingHttpResponse(open(url, "rb"))
        r["content_type"] = "application/octet-stream;charset=UTF-8"
        r["Content-Disposition"] = "attachment;filename=" + escape_uri_path(str(data[0].name))
        return r
    except Exception:
        raise Http404("Download error")


@csrf_exempt
def get_request_info(request):
    """
    获取该request的一些信息
    :param request:
    :return:
    """

    data = get_api_info.main(request)
    return HttpResponse(data)


def birthday_counter(request):
    return render(request, 'birthday/index.html')
