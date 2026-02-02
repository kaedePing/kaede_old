from django.conf.urls import url
from summary import views

urlpatterns = [
    url(r'^original/summaries$', views.SummaryOriginalListView.as_view()),
    url(r'^original/summaries/(?P<pk>\d+)$', views.SummaryOriginalDetailView.as_view()),

    url(r'^standard/summaries$', views.SummaryStandardListView.as_view()),
    url(r'^standard/summaries/(?P<pk>\d+)$', views.SummaryStandardDetailView.as_view()),

    url(r'special/summaries/random/(?P<pk>\d+)$', views.SummarySpecialDetailView.as_view()),
]
