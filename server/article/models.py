from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)  # 文章标题
    description = models.CharField(max_length=20)  # 文章简介
    last_up_date = models.DateField(default=None)  # 最后更新日期
    cover_url = models.URLField(
        default='https://i2.hdslb.com/bfs/face/2c28f8d11c0bd7920cd585976c0c61b7f9143c32.jpg')  # 文章封面地址
    address = models.CharField(max_length=20)  # 该文章地址

    class Meta:
        db_table = 'app_articles'
