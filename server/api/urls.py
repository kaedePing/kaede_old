from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^original/apis$', views.ApiOriginalListView.as_view()),
    url(r'^original/apis/(?P<pk>\d+)$', views.ApiOriginalDetailView.as_view()),

    url(r'^standard/apis$', views.ApiStandardListView.as_view()),
    url(r'^standard/apis/(?P<pk>\d+)$', views.ApiStandardDetailView.as_view()),
]
