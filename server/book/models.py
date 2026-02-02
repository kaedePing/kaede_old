from django.db import models
import datetime


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)  # 书籍名
    cover = models.URLField(default='http://49.234.15.210/static/web/articles/cover.jpg')  # 文章封面
    author = models.CharField(max_length=40)  # 作者
    nationality = models.CharField(max_length=20)  # 作者国籍
    translator = models.CharField(max_length=20)  # 译者
    startingTime = models.DateField(default=None)  # 开始时间
    endTime = models.DateField(default=None)  # 结束时间
    summary = models.CharField(max_length=2000)  # 总结

    class Meta:
        db_table = 'app_books'
