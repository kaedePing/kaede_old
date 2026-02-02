from rest_framework.serializers import ModelSerializer
from document.models import Document
from rest_framework import serializers
import os
import json
import requests
import time
import pymysql
from others.common.processor import get_token  # 引入专门获取token的程序


class DocumentSerializers(ModelSerializer):
    class Meta:
        model = Document  # 指定需要校验的模型
        fields = '__all__'  # 校验所有字段 同时可以指定admin后台展示哪些字段

    @staticmethod
    def get_file_name_order():
        """
        直接根据序号来命名存入服务器
        获取服务器中存放在文件目录下的文件名称，
        为确保规范和安全，客户端传过来的所有文件统一按服务器从小到大规则命名,即数字递增
        :return: 下一个应该保存的文件名称
        """
        last = ''
        result = []  # 用来存储提取的文件名称
        # 获取服务器中存放在文件目录下的文件
        path = os.getcwd() + '/others/document/media'
        file = os.listdir(path)
        for i in file:
            string = i.split('.')
            style = string[-1]
            string.remove(style)
            name = string[0]
            try:
                result.append(int(name))
            except Exception:
                continue
        if len(result) == 0:
            # 如果文件目录没有，则1就是下一个文件名称
            last = '1'
        else:
            result.sort(reverse=True)
            last = str(result[0] + 1)
        return last

    @staticmethod
    def get_file_name_default(name, style):
        """
        基于原来的文件名基础保存
        1.传入客户端上传的文件名
        2.根据文件名判断在服务器中是否已经存在，存在则在文件名后面添加 下划线+数字的形式
        :return: 该文件最后存在于服务器中的名称
        """
        origin = name + '.' + style
        new = origin
        path = os.getcwd() + '/others/document/media'
        file = os.listdir(path)
        if origin not in file:
            new = origin
        else:
            count = 1
            while True:
                temp = name + '_' + str(count) + '.' + style
                if temp not in file:
                    new = temp
                    break
                else:
                    count += 1
        return new

    @staticmethod
    def create_downloadLink(file_id):
        """
        传入某个文件的id，更新downloadLink字段，有两种方式更新
        1).根据对应的object直接update
        2).通过连接数据库的方式更新该数据
        :return:
        """
        direct_types = ['txt', 'py', 'vue', 'jpg', 'png', 'jpeg', 'ico', 'cmd', 'mp3']
        data = Document.objects.filter(id=file_id)
        original_type = data[0].originalType
        original_type = original_type.lower()
        if original_type in direct_types:
            url = "http://49.234.15.210/documents/download/" + str(file_id)
        else:
            url = "http://49.234.15.210/others/document/" + str(data[0].file)
        # 1).使用object直接更新
        data.update(downloadLink=url)

        # # 2).连接数据库刷这个字段
        #
        # # 1.连接MYSQL
        # conn = pymysql.connect(host="49.234.15.210", port=3306, user='root', passwd="Ping.1235", charset='utf8',
        #                        db='kaede')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #
        # # 2.发送指令
        # sql = "update app_documents set downloadLink=" + "'" + url + "'" + " where 1=1 and id=" + str(file_id)
        # cursor.execute(sql)
        # conn.commit()
        #
        # # 3.关闭
        # cursor.close()
        # conn.close()

    def validate(self, attrs):
        """
        校验前端传来的文件相关信息 主要校验上传的文件类型是否安全
        1.提取上传过来的 原文件名 源文件类型
        2.对origin字段赋值为传过来的文件名+文件类型
        3.赋值文件名称
        4.赋值文件类型
        5.对日期字段进行格式化限定
        6.对file字段基于原文件名后面添加数字递增的规则赋值
        7.最后根据客户端的token 分别判断是否满足类型安全
        :param attrs:
        :return:
        """
        # print(attrs['file'].name)  # 获取文件名
        # print(attrs['file'].size)  # 获取文件大小
        # print(attrs['file'].url )  # 获取文件url

        # 1.首先提取客户端传来的原文件名称和类型
        string = attrs['file'].name.split('.')
        style = string[-1]
        string.remove(string[-1])
        name = '.'.join(string)

        # 2.根据提取的原文件名称和类型对 原文件全称赋值
        attrs['origin'] = name + '.' + style

        # 3.赋值 文件名称
        attrs['originalName'] = name

        # 4.赋值 文件类型
        attrs['originalType'] = style

        # 5.对日期字段进行格式化限定
        attrs['dateCreatedStr'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        # 6.获取服务器中存放文件目录下的最大序号数，并赋值给该文件的file.name字段
        attrs['file'].name = DocumentSerializers.get_file_name_default(name, style)

        # 7.校验上传的类型必须在以下几种类型
        common = ['txt', 'jpg', 'png', 'jpeg', 'ico',
                  'html', 'css', 'py', 'vue', 'rar',
                  'exe', 'doc', 'docx',
                  'pdf', 'pptx', 'xlsx', 'csv', 'xls', 'chm', 'chw', 'mp3']
        # token = attrs['']

        if style not in common:
            raise serializers.ValidationError('非法上传')

        return attrs
