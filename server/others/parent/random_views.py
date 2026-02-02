# -*- coding: utf-8 -*-
# @Time : 2022/6/21 11:13
# @Author : kaede
# @File : random_views.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
#
# 用来返回一条随机的数据views
# 1.没有list列表
# 2.返回一条随机数据
#
# -*- Description -*-
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.versioning import URLPathVersioning
from rest_framework.filters import OrderingFilter
import random as rand


class DetailView(GenericAPIView):
    """
    detail视图访问的父类
    """

    def __init__(self, model, serializer_class, permission_classes=AllowAny):
        self.queryset = model.objects.all()  # 指定查询集
        self.serializer_class = serializer_class  # 指定序列化器类
        self.permission_classes = [permission_classes]  # 访问限制
        self.model = model  # 设置模型类

    def get(self, request, pk):
        """
        查询单个id
        """
        data = self.queryset
        ids = []
        for i in data:
            ids.append(i.id)
        result = rand.choice(ids)  # 随机获取一个id返回给前端
        data = self.model.objects.filter(id=result)[0]
        serializer = self.get_serializer(data)  # 传入查询到的数据，获取序列化器实列
        return Response(serializer.data)  # 返回查询到的单个id的值
