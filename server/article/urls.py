from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^original/articles$', views.ArticleOriginalListView.as_view()),
    url(r'^original/articles/(?P<pk>\d+)$', views.ArticleOriginalDetailView.as_view()),

    url(r'^standard/articles$', views.ArticleStandardListView.as_view()),
    url(r'^standard/articles/(?P<pk>\d+)$', views.ArticleStandardDetailView.as_view()),
]
