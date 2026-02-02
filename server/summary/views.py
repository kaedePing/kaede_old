from django.shortcuts import render

# Create your views here.
from summary.models import Summary
from summary.serializers import SummarySerializers
from others.parent import standard_views, original_views, random_views  # 引入自己编写的view父类
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse, Http404


# Create your views here.
class SummaryOriginalListView(original_views.ListView):
    def __init__(self):
        super().__init__(Summary.objects.all(), SummarySerializers, ['id', 'date'],
                         ['id', 'date'])


class SummaryOriginalDetailView(original_views.DetailView):
    def __init__(self):
        super().__init__(Summary.objects.all(), SummarySerializers, IsAuthenticated)


class SummaryStandardListView(standard_views.ListView):
    def __init__(self):
        super().__init__(Summary.objects.all(), SummarySerializers, ['id', 'date'],
                         ['id', 'date'])


class SummaryStandardDetailView(standard_views.DetailView):
    def __init__(self):
        super().__init__(Summary.objects.all(), SummarySerializers, IsAuthenticated)


class SummarySpecialDetailView(random_views.DetailView):
    def __init__(self):
        super().__init__(Summary, SummarySerializers)
