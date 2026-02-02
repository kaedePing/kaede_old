from django.db import models
import django


# Create your models here.
class MusicKuGou(models.Model):
    flag = models.CharField(verbose_name='是否启用', max_length=50, default='aaa')  # 是否失效标识
    sing_title = models.CharField(verbose_name='歌名', max_length=50, default='aaa')  # 歌名
    singer = models.CharField(verbose_name='歌手', max_length=50, default='aaa')  # 歌手
    format_sing_title = models.CharField(verbose_name='格式化后的歌名', max_length=50, default='aaa')  # 格式化后的歌名
    format_singer = models.CharField(verbose_name='格式化后的歌手', max_length=50, default='aaa')  # 格式化后的歌手
    name = models.CharField(verbose_name='歌曲完整信息', max_length=100, default='aaa')  # 歌曲完整信息
    playLink = models.URLField(verbose_name='播放地址', max_length=100,
                               default='http://49.234.15.210/static/web/articles/cover.jpg')  # 播放地址
    downloadUrl = models.URLField(verbose_name='下载地址', max_length=100,
                                  default='http://49.234.15.210/static/web/articles/cover.jpg')  # 下载地址
    originDownloadUrl = models.URLField(verbose_name='原下载地址', max_length=240,
                                        default='http://49.234.15.210/static/web/articles/cover.jpg')  # 原下载地址
    dateCreated = models.DateTimeField(verbose_name='上传日期', auto_now_add=True)  # 创建日期
    dateCreatedStr = models.CharField(verbose_name='上传日期(年月日时分秒)', max_length=50,
                                      default='2023-02-27 00:00:00')  # 创建日期(年月日时分秒)

    class Meta:
        db_table = 'app_music_v1s'  # 酷狗music


class RequestInfo(models.Model):
    method = models.CharField(verbose_name='请求方法', max_length=10, default='GET')  # 请求方法
    path = models.CharField(verbose_name='路径', max_length=50, default='aaa')  # 请求地址
    query_string = models.CharField(verbose_name='查询字符串', max_length=1000, default='')  # 查询字符串
    get_or_post_param = models.CharField(verbose_name='get or post参数', max_length=1000, default='')  # get or post参数
    ip = models.CharField(verbose_name='ip', max_length=50, default='aaa')  # ip
    continent = models.CharField(verbose_name='大洲', max_length=240, default='aaa')  # 大洲
    country_code = models.CharField(verbose_name='国家或地区代码', max_length=240, default='aaa')  # 国家或地区代码
    country_name = models.CharField(verbose_name='国家或地区名称', max_length=240, default='aaa')  # 国家或地区名称
    area_name = models.CharField(verbose_name='地区名称', max_length=240, default='aaa')  # 地区名称
    city_name = models.CharField(verbose_name='城市名称', max_length=240, default='aaa')  # 城市名称
    city_latitude = models.CharField(verbose_name='城市纬度', max_length=50, default='aaa')  # 城市纬度
    city_longitude = models.CharField(verbose_name='城市经度', max_length=50, default='aaa')  # 城市经度
    service_provider = models.CharField(verbose_name='服务商', max_length=240, default='aaa')  # 服务商
    dateCreated = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)  # 创建日期
    dateCreatedStr = models.CharField(verbose_name='创建日期(年月日时分秒)', max_length=50,
                                      default='2023-02-27 00:00:00')  # 创建日期(年月日时分秒)

    class Meta:
        db_table = 'app_request_infos'  # 请求的其他信息
