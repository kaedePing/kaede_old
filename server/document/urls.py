from django.conf.urls import url
from document import views

urlpatterns = [
    url(r'^original/documents$', views.DocumentOriginalListView.as_view()),
    url(r'^original/documents/(?P<pk>\d+)$', views.DocumentOriginalDetailView.as_view()),

    url(r'^standard/documents$', views.DocumentStandardListView.as_view()),
    url(r'^standard/documents/(?P<pk>\d+)$', views.DocumentStandardDetailView.as_view()),

    url(r'^special/documents/(?P<pk>\d+)$', views.DocumentSpecialDetailView.as_view()),  # 专门用来删除该条数据的接口

    url(r'^special/documents/download/(?P<pk>\d+)$', views.download),  # 下载
]
