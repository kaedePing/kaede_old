from django.db import models


# Create your models here.
class Summary(models.Model):
    title = models.CharField(max_length=100, default=None)  # 书籍名
    author = models.CharField(max_length=50, default=None)  # 作者
    summary = models.CharField(max_length=2000)  # 经典句子
    date = models.DateField(default=None)  # 记录日期

    class Meta:
        db_table = 'app_summaries'
