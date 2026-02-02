from django.db import models


# Create your models here.
class Api(models.Model):
    app = models.CharField(max_length=20, verbose_name='应用')  # 哪个应用
    method = models.CharField(max_length=20, verbose_name='请求方法')  # 方法
    url = models.URLField(default='http://49.234.15.210/', verbose_name='请求地址')  # 请求地址
    description = models.CharField(max_length=240, verbose_name='请求描述')  # 请求描述
    dateCreated = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)  # 创建日期
    dateUpdate = models.DateTimeField(verbose_name='修改日期', auto_now=True)  # 修改日期
    dateCreatedStr = models.CharField(verbose_name='创建日期(年月日时分秒)', max_length=50,
                                      default='2023-02-27 00:00:00')  # 创建日期(年月日时分秒)

    class Meta:
        db_table = 'app_apis'
