from django.shortcuts import render

# Create your views here.
from article.models import Article
from article.serializers import ArticleSerializers
from others.parent import standard_views, original_views  # 引入自己编写的view父类
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class ArticleOriginalListView(original_views.ListView):
    def __init__(self):
        super().__init__(Article.objects.all(), ArticleSerializers, ['id', 'title', 'last_up_date'],
                         ['id', 'title', 'last_up_date'])


class ArticleOriginalDetailView(original_views.DetailView):
    def __init__(self):
        super().__init__(Article.objects.all(), ArticleSerializers, IsAuthenticated)


class ArticleStandardListView(standard_views.ListView):
    def __init__(self):
        super().__init__(Article.objects.all(), ArticleSerializers, ['id', 'title', 'last_up_date'],
                         ['id', 'title', 'last_up_date'])


class ArticleStandardDetailView(standard_views.DetailView):
    def __init__(self):
        super().__init__(Article.objects.all(), ArticleSerializers, IsAuthenticated)
