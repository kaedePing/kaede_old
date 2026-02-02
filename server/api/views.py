from django.shortcuts import render

# Create your views here.
from api.models import Api
from api.serializers import ApiSerializers
from others.parent import standard_views, original_views
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class ApiOriginalListView(original_views.ListView):
    def __init__(self):
        super().__init__(Api.objects.all(), ApiSerializers, ['id', 'app', 'method', 'dateCreated', 'dateUpdate'],
                         ['id', 'app', 'method', 'dateCreated', 'dateUpdate'])


class ApiOriginalDetailView(original_views.DetailView):
    def __init__(self):
        super().__init__(Api.objects.all(), ApiSerializers, IsAuthenticated)


class ApiStandardListView(standard_views.ListView):
    def __init__(self):
        super().__init__(Api.objects.all(), ApiSerializers, ['id', 'app', 'method', 'dateCreated', 'dateUpdate'],
                         ['id', 'app', 'method', 'dateCreated', 'dateUpdate'])


class ApiStandardDetailView(standard_views.DetailView):
    def __init__(self):
        super().__init__(Api.objects.all(), ApiSerializers, IsAuthenticated)
