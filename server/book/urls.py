from django.conf.urls import url
from book import views

urlpatterns = [
    url(r'^original/books$', views.BookOriginalListView.as_view()),
    url(r'^original/books/(?P<pk>\d+)$', views.BookOriginalDetailView.as_view()),

    url(r'^standard/books$', views.BookStandardListView.as_view()),
    url(r'^standard/books/(?P<pk>\d+)$', views.BookStandardDetailView.as_view()),
]
