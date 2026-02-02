from django.db import models
import django


# Create your models here.
class Document(models.Model):
    file = models.FileField(verbose_name='服务器文件', upload_to='media')  # 保存文件的地址 upload_to 指定 MEDIA_ROOT 下的子目录
    downloadLink = models.URLField(verbose_name='下载地址', max_length=100,
                                   default='http://49.234.15.210/static/web/articles/cover.jpg')  # 前端访问可以直接下载的地址
    origin = models.CharField(verbose_name='原文件全称', max_length=50, default='aaa')  # 上传的文件全称(名字+后缀)
    originalName = models.CharField(verbose_name='原文件名称', max_length=50, default='aaa')  # 上传的文件名称
    originalType = models.CharField(verbose_name='原文件类型', max_length=20, default='txt')  # 上传的原文件类型
    dateCreated = models.DateTimeField(verbose_name='上传日期', auto_now_add=True)  # 上传日期
    dateCreatedStr = models.CharField(verbose_name='上传日期(年月日时分秒)', max_length=50,
                                      default='2022-06-14 00:00:00')  # 上传日期(年月日时分秒)

    class Meta:
        db_table = 'app_documents'
