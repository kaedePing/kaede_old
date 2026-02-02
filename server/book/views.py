from django.shortcuts import render

# Create your views here.
from book.models import Book
from book.serializers import BookSerializers
from others.parent import standard_views, original_views  # 引入自己编写的view父类
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class BookOriginalListView(original_views.ListView):
    def __init__(self):
        super().__init__(Book.objects.all(), BookSerializers, ['id', 'title', 'nationality'],
                         ['id', 'title', 'nationality'])


class BookOriginalDetailView(original_views.DetailView):
    def __init__(self):
        super().__init__(Book.objects.all(), BookSerializers, IsAuthenticated)


# Create your views here.
class BookStandardListView(standard_views.ListView):
    def __init__(self):
        super().__init__(Book.objects.all(), BookSerializers, ['id', 'title', 'nationality'],
                         ['id', 'title', 'nationality'])


class BookStandardDetailView(standard_views.DetailView):
    def __init__(self):
        super().__init__(Book.objects.all(), BookSerializers, IsAuthenticated)
