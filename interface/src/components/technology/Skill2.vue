<template>
  <div class="skill2">
    <h1 style="margin-left: 40%">Django</h1>
    <ol style="list-style-type: none;margin-top: 2px">
      <li>
        <h2 id="foreword">一.前言</h2>
        <p style="text-indent: 2em;margin-top: 5px">
          此篇博客介绍一个Django项目的基本流程，包括创建项目、创建应用(APP)也就是一个接口的流程、主要文件的作用；
          以及Django进阶部分，包括认证、限流、分页、自动生成接口文档等。
        </p>
      </li>
      <br>

      <li>
        <h2 id="DjangoBasicDevelopmentProcess">二.Django基本开发流程</h2>
        <p style="text-indent: 2em;margin-top: 5px">
          一个Django项目可以理解为两部分，项目(project)、应用(app)。
        </p>
        <p style="text-indent: 2em;margin-top: 5px">
          项目就相当于一个Django项目初始化的基本文件，项目里面控制整个框架的运转流程、基本配置，比如静态资源、数据库配置、加载哪些app等。
        </p>
        <p style="text-indent: 2em;margin-top: 5px">
          应用可以理解为一个类型的接口，比如一个Django项目主要用于提供电影等信息，就可以将电影当作一个应用，去单独处理该接口的内容，方便管理维护接口信息。
        </p>
        <p style="text-indent: 2em;margin-top: 5px">
          一个Django项目可以有多个应用，应用必须在项目里面加载、配置其路由信息，客户端才能访问该应用即接口。
          首先客户端访问url，Django项目接收信息，从项目中的urls去寻找访问的是哪个url，然后去找到指定app下的urls，
          urls就会去访问views文件，views通过models和serializers文件去处理接口信息返回给前端，一个接口流程就运行完成。
        </p>
        <br>
        <ol style="margin-left: 2%">

          <li>
            <h3 id="createProject">创建project</h3>
            <p style="text-indent: 2em;margin-top: 5px">
              使用命令 django-admin startproject server 创建一个Django基本项目，整个项目最外层的文件名就叫server，
              内部还有一个server文件夹，该Django项目需要做的配置就在该server文件夹下对应的settings.py和urls.py文件。
            </p>
            <ul style="margin-left: 2%;list-style-type: disc">
              <li>
                <h4 id="DatabaseConfiguration">数据库配置</h4>
                <p style="text-indent: 2em;margin-top: 5px">
                  Django有默认的数据库配置sqlite，可以自行修改为其他数据库(需要开放数据库的其他主机连接权限)，比如下面就是连接mysql数据库
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data1">{{
                    item
                  }}</span></pre>
              </li>

              <li>
                <h4 id="RegisterToLoadTheApp">注册加载应用</h4>
                <p style="text-indent: 2em;margin-top: 5px">
                  在settings.py文件里需要注册创建的app，比如下面就是注册创建的movie应用
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data2">{{
                    item
                  }}</span></pre>
              </li>

              <li>
                <h4 id="defineRoutes">定义路由</h4>
                <p style="text-indent: 2em;margin-top: 5px">
                  在urls.py文件里定义整个Django项目的路由，加载创建的app路由，使用include将整个app下的ursl加载进来
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data3">{{
                    item
                  }}</span></pre>
              </li>
            </ul>
          </li>
          <br>

          <li>
            <h3 id="createApp">创建app</h3>
            <p style="text-indent: 2em;margin-top: 5px">
              使用命令 django-admin startapp movie 创建一个叫movie的app，
              默认文件主要使用models和views，还需要创建serializers和urls两个py文件。
              项目下的urls调用每个app下的urls，然后就是一个app内部各个文件的调用。
              urls调用views，views调用models和serializers返回内容即可。
            </p>
            <ul style="margin-left: 2%;list-style-type: disc">
              <li>
                <h4 id="modelsFile">models文件</h4>
                <p style="text-indent: 2em;margin-top: 5px">
                  models(模型)是整个应用以及接口的基准，里面定义接口存储在数据库中的具体字段，以及表名等，每个字段的类型直接网络百度即可，
                  类需要继承models.Model，类中每一个变量就是一个字段，不需要专门去定义主键，它会自己默认一个id为主键，同时通过接口实现插入数据时会实现自增长。
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data4">{{
                    item
                  }}</span></pre>
              </li>

              <li>
                <h4 id="serializersFile">serializers文件</h4>
                <p style="text-indent: 2em;margin-top: 5px">
                  序列化器，主要就是校验前端传过来的字段，除了继承类的默认校验外，还可以自定义校验，
                  需要注意的就是自定义校验时，需要返回原来传过来的值即参数(参数里面的内容可以修改)。
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data5">{{
                    item
                  }}</span></pre>
              </li>

              <li>
                <h4 id="viewsFile">views文件</h4>
                <p style="text-indent: 2em;margin-top: 5px">
                  每个app下面的views文件几乎都是一样的，因此可以单独提取出来做一个父类，其他组件调用传入各个应用自己的内容即可，
                  下面的例子包含一些进阶部分，跟着代码注释查看即可，需要配合设置settings.py文件，参考后面进阶部分。首先就是定义的父类文件
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data6">{{
                    item
                  }}</span></pre>
                <p style="text-indent: 2em;margin-top: 5px">
                  应用继承父类views
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data7">{{
                    item
                  }}</span></pre>
              </li>

              <li>
                <h4 id="urlsFile">urls文件</h4>
                <p style="text-indent: 2em;margin-top: 5px">
                  前端访问的url会定位到该文件具体的路由，然后调用views返回对应的内容即可
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data8">{{
                    item
                  }}</span></pre>
              </li>

            </ul>
          </li>

        </ol>
      </li>
      <br>

      <li>
        <h2 id="AdvancedPart">三.高阶部分</h2>
        <p style="text-indent: 2em;margin-top: 5px">
          关于模板加载那块以及静态文件配置，可以查看另外一篇专门介绍博客的文章，静态文件问题以及Vue与Django联调部分，
          使用的话就参考
          <a href="#viewsFile">views</a>即可。
          首先需要在settings.py文件里配置，下面是一些经常会使用的限制，
        </p>
        <ul style="list-style-type: disc;margin-left: 2%">
          <li>
            <h3 id="LoadComponents">加载组件</h3>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data9">{{
                item
              }}</span></pre>
          </li>
          <li>
            <h3 id="ConfigureTheCorrespondingInformation">配置相应信息</h3>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data10">{{
                item
              }}</span></pre>
            <p style="text-indent: 2em;margin-top: 5px">
              pagination文件内容，用于分页(与manage.py同级)
            </p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data11">{{
                item
              }}</span></pre>
          </li>
        </ul>

        <ol style="margin-left: 2%">
          <li>
            <h3 id="AutomaticInterfaceDocumentation">自动接口文档</h3>
            <p style="text-indent: 2em;margin-top: 5px">
              进阶部分settings文件REST_FRAMEWORK里面有配置自动生成接口文档，还需要在urls文件里定义路由
            </p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data12">{{
                item
              }}</span></pre>
          </li>

          <li>
            <h3 id="uploadFiles">上传文件</h3>
            <p style="text-indent: 2em;margin-top: 5px">
              Django接口可以定义一个文件类型，上传的文件放在upload_to文件下，在model设置如下
            </p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data13">{{
                item
              }}</span></pre>
            <p style="text-indent: 2em;margin-top: 5px">
              Settings配置上传文件的路径，以及用MEDIA_URL访问文件
            </p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data14">{{
                item
              }}</span></pre>
          </li>

          <li>
            <h3 id="timeZoneSetting">时区设置</h3>
            <p style="text-indent: 2em;margin-top: 5px">
              Django的模型文件可以定义时间类型，需要默认配置会差8个小时，数据库实际存储与接口展示不一致的问题，修改Setting文件
            </p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data15">{{
                item
              }}</span></pre>

          </li>

        </ol>

      </li>

    </ol>
  </div>
</template>

<script>
export default {
  name: "ComponentsTechnologySkill2",
  data() {
    return {
      data1: ['DATABASES = {',
        '    \'default\': {',
        '        \'ENGINE\': \'django.db.backends.mysql\',',
        '        \'NAME\': \'interface\',',
        '        \'USER\': \'user\',',
        '        \'PASSWORD\': \'password\',',
        '        \'HOST\': \'localhost\',',
        '        \'PORT\': \'3306\',',
        '    }',
        '}',
      ],
      data2: ['INSTALLED_APPS = [',
        '    \'django.contrib.admin\',',
        '    \'django.contrib.auth\',',
        '    \'django.contrib.contenttypes\',',
        '    \'django.contrib.sessions\',',
        '    \'django.contrib.messages\',',
        '    \'django.contrib.staticfiles\',',
        '',
        '    \'movie\',  # 注册创建的app',
        '    \'rest_framework\',  # 方便使用其完整的序列化流程，包括序列化器、视图类，免去了很多流程操作',
        '    \'django_filters\',  # 用于过滤',
        '    \'rest_framework.authtoken\',  # 用于认证限流',
        ']',
      ],
      data3: ['from django.contrib import admin',
        'from django.urls import path, include',
        '',
        'urlpatterns = [',
        '    path(\'\', include(\'movie.urls\')),  # 加载应用movie下的urls',
        ']',
      ],
      data4: ['from django.db import models',
        '',
        '',
        '# Create your models here.',
        '',
        'class MovieWhole(models.Model):',
        '    name = models.CharField(max_length=50)  # 电影名',
        '    box = models.DecimalField(max_digits=10, decimal_places=2)  # 票房(万元)',
        '    avg_fare = models.DecimalField(max_digits=5, decimal_places=2)  # 平均票价(元)',
        '    avg_players = models.DecimalField(max_digits=5, decimal_places=0)  # 场均人次',
        '    url = models.URLField()  # 电影详情页',
        '',
        '    class Meta:',
        '        db_table = \'movie_whole\'  # 表名',
      ],
      data5: ['from rest_framework.serializers import ModelSerializer',
        'from movie import models',
        '',
        '',
        'class MovieWholeSerializer(ModelSerializer):',
        '    class Meta:',
        '        model = models.MovieWhole  # 校验哪个模型',
        '        fields = \'__all__\'  # 校验所有字段',
        '',
        '    def validate(self, attrs):',
        '        """',
        '        自定义校验方法，需返回同样的参数',
        '        """',
        '        print(attrs[\'name\'])  # 输出前端传入的name字段',
        '        return attrs',
      ],
      data6: ['from rest_framework.generics import GenericAPIView',
        'from rest_framework.response import Response',
        'from rest_framework.permissions import IsAuthenticated, AllowAny',
        'from django_filters.rest_framework import DjangoFilterBackend',
        'from rest_framework import status',
        'from rest_framework.versioning import URLPathVersioning',
        '',
        '',
        '# Create your views here.',
        'class ListView(GenericAPIView):',
        '    """',
        '    list视图访问的父类',
        '    """',
        '    filter_backends = [DjangoFilterBackend]  # 指定过滤器',
        '    versioning_class = URLPathVersioning  # 指定版本控制相关的类',
        '',
        '    def __init__(self, queryset, serializer_class, filter_fields,permission=AllowAny):',
        '        self.queryset = queryset  # 指定查询集',
        '        self.serializer_class = serializer_class  # 指定序列化器类',
        '        self.filter_fields = filter_fields  # 指定可过滤的字段',
        '        self.permission_classes=[permission]  # 指定改视图允许的访问权限',
        '',
        '    def get(self, request, *args, **kwargs):',
        '        """',
        '        前端get请求获取该接口内容',
        '        :param request:',
        '        :param args:',
        '        :param kwargs:',
        '        :return:',
        '        """',
        '        version = request.version  # 获取前端传入的版本号，默认为\'v1\'',
        '        if version == \'v1\':',
        '            data = self.get_queryset()  # 获取查询集的内容',
        '            filter_data = self.filter_queryset(data)  # 过滤字段',
        '            page = self.paginate_queryset(filter_data)  # 分页',
        '            if page is not None:',
        '                filter_serializer = self.get_serializer(page, many=True)  # 传入分页后的数据给序列化器，获取一个实列',
        '                return self.get_paginated_response(filter_serializer.data)  # 返回分页后的数据',
        '            serializer = self.get_serializer(data, many=True)',
        '            return Response(serializer.data)',
        '        else:',
        '            return Response(\'请输入正确的版本号!\')',
        '',
        '    def post(self, request):',
        '        """',
        '        接收前端的post请求，将数据存入到接口中',
        '        :param request:',
        '        :return:',
        '        """',
        '        data = request.data',
        '        if isinstance(data, list):  # list类型表示有很多条数据',
        '            many = True',
        '        elif isinstance(data, dict):  # dict类型表示只有一条数据',
        '            many = False',
        '        else:  # 其它数据格式则认为是错误的',
        '            return Response(\'请传入正确的数据格式\')',
        '        serializer = self.get_serializer(data=data, many=many)  # 传入数据，获取序列化器的实列',
        '        serializer.is_valid(raise_exception=True)  # 校验字段，可以自行在序列化器中写校验方法，如果有错，直接报错，不会再执行下面的save',
        '        serializer.save()  # is_valid如果没报错，就直接保存数据',
        '        return Response(serializer.data)',
        '',
        '',
        'class DetailView(GenericAPIView):',
        '    """',
        '    detail视图访问的父类',
        '    """',
        '',
        '    def __init__(self, queryset, serializer_class,permission=AllowAny):',
        '        self.queryset = queryset  # 指定查询集',
        '        self.serializer_class = serializer_class  # 指定序列化器类',
        '        self.permission_classes = [permission]  # 指定改视图允许的访问权限',
        '',
        '    def get(self, request, pk):',
        '        """',
        '        查询单个id',
        '        """',
        '        data = self.get_object()  # 获取查询到的单个id数据',
        '        serializer = self.get_serializer(data)  # 传入查询到的数据，获取序列化器实列',
        '        return Response(serializer.data)  # 返回查询到的单个id的值',
        '',
        '    def put(self, request, pk):',
        '        """',
        '        修改单个id',
        '        """',
        '        data = self.get_object()  # 获取查询的单个id数据',
        '        serializer = self.get_serializer(data, request.data)  # 传入数据，获取序列化器实列',
        '        serializer.is_valid(raise_exception=True)  # 校验字段',
        '        serializer.save()  # 保存数据',
        '        return Response(serializer.data)  # 返回修改的数据',
        '',
        '    def delete(self, request, pk):',
        '        """',
        '        删除单个id',
        '        """',
        '        data = self.get_object()  # 获取查询的单个id数据',
        '        data.delete()  # 删除查询到的数据',
        '        return Response(status=status.HTTP_204_NO_CONTENT)  # 返回删除后的状态码',
      ],
      data7: ['from django.shortcuts import render',
        'from rest_framework.permissions import IsAuthenticated, AllowAny',
        'from movie import models',
        'from movie import serializers',
        'from father import view',
        '',
        '# Create your views here.',
        'filter_fields = [\'id\', \'name\']  # 设定下面所有list的过滤字段',
        '',
        '# list',
        'class MovieWholeListView(view.ListView):',
        '    def __init__(self):',
        '        super().__init__(models.MovieWhole.objects.all(), serializers.MovieWholeSerializer, filter_fields)',
        '',
        '# detail',
        'class MovieWholeDetailView(view.DetailView):',
        '    def __init__(self):',
        '        super().__init__(models.MovieWhole.objects.all(), serializers.MovieWholeSerializer,IsAuthenticated)',
      ],
      data8: ['from django.conf.urls import url',
        'from movie import views',
        '',
        'urlpatterns = [',
        '    url(r\'^movie/whole/$\', views.MovieWholeListView.as_view()),  # 完整列表',
        '    url(r\'^movie/whole/(?P<pk>\d+)/$\', views.MovieWholeDetailView.as_view()),  # 单个详细列表',
        ']',
      ],
      data9: ['INSTALLED_APPS = [',
        '    \'django.contrib.admin\',',
        '    \'django.contrib.auth\',',
        '    \'django.contrib.contenttypes\',',
        '    \'django.contrib.sessions\',',
        '    \'django.contrib.messages\',',
        '    \'django.contrib.staticfiles\',',
        '',
        '    \'rest_framework\',  # 需要使用其内部封装完成度高的类',
        '    \'django_filters\',  # 过滤器',
        '    \'rest_framework.authtoken\',  # 认证限流',
        ']',
      ],
      data10: ['REST_FRAMEWORK = {',
        '    \'DEFAULT_AUTHENTICATION_CLASSES\': (  # 认证类',
        '        \'rest_framework.authentication.BasicAuthentication\',',
        '        \'rest_framework.authentication.SessionAuthentication\',',
        '        \'rest_framework.authentication.TokenAuthentication\',',
        '    ),',
        '    \'DEFAULT_THROTTLE_CLASSES\': (  # 指定限流类',
        '        \'rest_framework.throttling.AnonRateThrottle\',',
        '        \'rest_framework.throttling.UserRateThrottle\',',
        '    ),',
        '    \'DEFAULT_THROTTLE_RATES\': {  # 限流措施',
        '        \'anon\': \'100/day\',',
        '        \'user\': \'100000/day\'',
        '    },',
        '    \'DEFAULT_PAGINATION_CLASS\': \'pagination.PageNumberPaginationManual\',  # 分页(需要定义一个pagination文件)',
        '    \'DEFAULT_SCHEMA_CLASS\': \'rest_framework.schemas.coreapi.AutoSchema\',  # 配置自动生成接口文档的默认配置',
        '    \'DEFAULT_VERSION\': \'v1\',  # 默认版本',
        '    \'ALLOWED_VERSIONS\': [\'v1\', \'v2\'],  # 允许的版本',
        '    \'VERSION_PARAM\': \'version\'  # URL中获取值的key',
        '}',
      ],
      data11: ['from rest_framework.pagination import PageNumberPagination',
        '',
        'class PageNumberPaginationManual(PageNumberPagination):',
        '    # page_query_param = \'p\'',
        '    page_size = 100',
        '    # page_size_query_param = \'s\'',
        '    max_page_size = 50',
      ],
      data12: ['from django.urls import path',
        'from rest_framework.documentation import include_docs_urls',
        '',
        'urlpatterns = [',
        '    path(\'docs/\', include_docs_urls(title=\'Api Document\')),  # 该路由就可以看到自动生成的接口',
        ']',
      ],
      data13: ['from django.db import models',
        'from server import settings',
        '',
        '',
        '# Create your models here.',
        'class UpFile(models.Model):',
        '    file = models.FileField(verbose_name=\'文件地址\',upload_to=\'media\')  # upload_to 指定 MEDIA_ROOT 下的子目录',
        '    origin = models.CharField(verbose_name=\'原文件名称\',max_length=200,default=\'aaa\')  # 上传的文件原名称',
        '    date = models.DateTimeField(verbose_name=\'上传日期\',auto_now=True)  # 上传日期',
        '',
        '    class Meta:',
        '        db_table = \'upFile\'',
      ],
      data14: ['# 上传文件的配置',
        'MEDIA_URL = \'/file/document/\'  # 与下面的 MEDIA_ROOT里面的值除了多两个/外，其它都要一样',
        'MEDIA_ROOT = os.path.join(BASE_DIR, \'file/document\')  # file/document文件是上传文件的根目录',
      ],
      data15: ['# 解决时区问题 Django admin展示以及数据库实际存储',
        'LANGUAGE_CODE = \'zh-hans\'',
        'TIME_ZONE = \'Asia/Shanghai\'',
        'USE_TZ = False',
      ]
    }
  }
}
</script>

<style>
.skill2 {
  width: 60%;
  float: left;
  margin-left: 30%;
  box-shadow: #666 0px 0px 10px 0px;
  position: relative;
}
</style>