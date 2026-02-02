from django.conf.urls import url
from interface import views, api_views

urlpatterns = [
    # Original
    url(r'^original/music/v1s$', views.MusicKuGouOriginalListView.as_view()),
    url(r'^original/music/v1s/(?P<pk>\d+)$', views.MusicKuGouOriginalDetailView.as_view()),
    url(r'^original/request/infos$', views.RequestInfoOriginalListView.as_view()),
    url(r'^original/request/infos/(?P<pk>\d+)$', views.RequestInfoOriginalDetailView.as_view()),

    # Standard
    url(r'^standard/music/v1s$', views.MusicKuGouStandardListView.as_view()),
    url(r'^standard/music/v1s/(?P<pk>\d+)$', views.MusicKuGouStandardDetailView.as_view()),
    url(r'^standard/request/infos$', views.RequestInfoStandardListView.as_view()),
    url(r'^standard/request/infos/(?P<pk>\d+)$', views.RequestInfoStandardDetailView.as_view()),

    url(r'^api/translate', api_views.translate),  # 对应的翻译接口
    url(r'^api/music/v1/search', api_views.search_music_v1),  # 酷狗音乐的搜索接口
    url(r'^api/music/v1/play/(?P<pk>\d+)$', api_views.get_music_v1_play),  # 酷狗音乐播放的接口
    url(r'^api/music/v1/download/(?P<pk>\d+)$', api_views.get_music_v1_download),  # 酷狗音乐下载的接口
    url(r'^api/request/info$', api_views.get_request_info),  # 对应的请求信息

    url(r'^temporary/birthday$', api_views.birthday_counter),  # 对应的请求信息

]
