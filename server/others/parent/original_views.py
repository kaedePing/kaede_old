# -*- coding: utf-8 -*-
# @Time : 2022/6/21 11:13
# @Author : kaede
# @File : original_views.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
#
# 一个初始的父类视图views，与标准的相比，没有分页操作
#
# -*- Description -*-
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.versioning import URLPathVersioning
from rest_framework.filters import OrderingFilter


# Create your views here.
class ListView(GenericAPIView):
    """
    list视图访问的父类
    """
    versioning_class = URLPathVersioning  # 指定版本控制相关的类
    filter_backends = (OrderingFilter, DjangoFilterBackend)  # 指定排序类,指定过滤器

    def __init__(self, queryset, serializer_class, filter_fields, ording_fields, permission_classes=AllowAny):
        self.queryset = queryset  # 指定查询集
        self.serializer_class = serializer_class  # 指定序列化器类
        self.filter_fields = filter_fields  # 指定可过滤的字段
        self.permission_classes = [permission_classes]  # 访问限制
        self.ording_fields = ording_fields  # 指定需要排序的字段

    def get(self, request, *args, **kwargs):
        version = request.version  # 获取前端传入的版本号，默认为'v1'
        if version == 'v1':
            data = self.get_queryset()  # 获取查询集的内容
            filter_data = self.filter_queryset(data)  # 过滤字段
            serializer = self.get_serializer(filter_data, many=True)
            return Response(serializer.data)
        else:
            return Response('请输入正确的版本号!')

    def post(self, request):
        data = request.data
        if isinstance(data, list):
            many = True
        elif isinstance(data, dict):
            many = False
        else:
            return Response('请传入正确的数据格式')
        serializer = self.get_serializer(data=data, many=many)  # 传入数据，获取序列化器的实列
        serializer.is_valid(raise_exception=True)  # 校验字段，可以自行在序列化器中写校验方法，如果有错，直接报错，不会再执行下面的save
        serializer.save()  # is_valid如果没报错，就直接保存数据
        return Response(serializer.data)


class DetailView(GenericAPIView):
    """
    detail视图访问的父类
    """

    def __init__(self, queryset, serializer_class, permission_classes=AllowAny):
        self.queryset = queryset  # 指定查询集
        self.serializer_class = serializer_class  # 指定序列化器类
        self.permission_classes = [permission_classes]  # 访问限制

    def get(self, request, pk):
        """
        查询单个id
        """
        data = self.get_object()  # 获取查询到的单个id数据
        serializer = self.get_serializer(data)  # 传入查询到的数据，获取序列化器实列
        return Response(serializer.data)  # 返回查询到的单个id的值

    def put(self, request, pk):
        """
        修改单个id
        """
        data = self.get_object()  # 获取查询的单个id数据
        serializer = self.get_serializer(data, request.data)  # 传入数据，获取序列化器实列
        serializer.is_valid(raise_exception=True)  # 校验字段
        serializer.save()  # 保存数据
        return Response(serializer.data)  # 返回修改的数据

    def delete(self, request, pk):
        """
        删除单个id
        """
        data = self.get_object()  # 获取查询的单个id数据
        data.delete()  # 删除查询到的数据
        return Response(status=status.HTTP_204_NO_CONTENT)  # 返回删除后的状态码
