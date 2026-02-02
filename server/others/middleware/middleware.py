# -*- coding: utf-8 -*-
"""
@Time    : 2026/2/1 14:46
@Author  : kaede
@Email   : flowerslanguage@126.com
@File    : middleware.py
@Description: Django定义中间件
"""
from django.utils.deprecation import MiddlewareMixin


def my1(func):
    def innner(request):
        print('~~~~before·~~~~~')
        res = func(request)
        print('~~~~after~~~~~~~')

        return res

    return innner


class My2:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        print('~~~~before~~~~~~')
        res = self.func(request)
        print('·~~~~after~~~~')

        return res


class My3(MiddlewareMixin):
    # 视图函数之前执行
    def process_request(self, request):
        print('before2')

    # 视图函数之后执行
    def process_response(self, request, response):
        print('after2')
        return response

    # 在视图函数之前，process_request之后执行
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('process_view')

    # 用来记录错误日志，视图函数中发生错误
    def process_exception(self, request, exception):
        print(str(exception))

    # 在视图函数之后，在 process_response之前
    def process_template_response(self, request, response):
        print('process_template_response')
        return response
