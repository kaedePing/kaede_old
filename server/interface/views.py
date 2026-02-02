from django.shortcuts import render
from rest_framework.response import Response
from interface.models import MusicKuGou, RequestInfo
from interface.serializers import MusicKuGouSerializers, RequestInfoSerializers
from others.parent import standard_views, original_views  # 引入自己编写的view父类
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
# Original
class MusicKuGouOriginalListView(original_views.ListView):
    def __init__(self):
        super().__init__(MusicKuGou.objects.all(), MusicKuGouSerializers,
                         ['id', 'flag', 'sing_title', 'singer', 'name'],
                         ['id', 'flag', 'sing_title'])


class MusicKuGouOriginalDetailView(original_views.DetailView):
    def __init__(self):
        super().__init__(MusicKuGou.objects.all(), MusicKuGouSerializers, IsAuthenticated)


class RequestInfoOriginalListView(original_views.ListView):
    def __init__(self):
        super().__init__(RequestInfo.objects.all(), RequestInfoSerializers,
                         ['id', 'ip'],
                         ['id', 'ip'])


class RequestInfoOriginalDetailView(original_views.DetailView):
    def __init__(self):
        super().__init__(RequestInfo.objects.all(), RequestInfoSerializers, IsAuthenticated)


# Standard
class MusicKuGouStandardListView(standard_views.ListView):
    def __init__(self):
        super().__init__(MusicKuGou.objects.all(), MusicKuGouSerializers,
                         ['id', 'flag', 'sing_title', 'singer', 'name'],
                         ['id', 'flag', 'sing_title'])


class MusicKuGouStandardDetailView(standard_views.DetailView):
    def __init__(self):
        super().__init__(MusicKuGou.objects.all(), MusicKuGouSerializers, IsAuthenticated)


class RequestInfoStandardListView(standard_views.ListView):
    def __init__(self):
        super().__init__(RequestInfo.objects.all(), RequestInfoSerializers,
                         ['id', 'ip'],
                         ['id', 'ip'])


class RequestInfoStandardDetailView(standard_views.DetailView):
    def __init__(self):
        super().__init__(RequestInfo.objects.all(), RequestInfoSerializers, IsAuthenticated)
