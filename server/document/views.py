import os

from django.shortcuts import render

# Create your views here.
from document.models import Document
from document.serializers import DocumentSerializers
from others.parent import standard_views, original_views, document_views  # 引入自己编写的view父类
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import StreamingHttpResponse, FileResponse
from django.http import HttpResponse, Http404
from django.utils.encoding import escape_uri_path  # 解决中文不能下载的问题


# Create your views here.
class DocumentOriginalListView(original_views.ListView):
    def __init__(self):
        super().__init__(Document.objects.all(), DocumentSerializers, ['id'], ['id'])


class DocumentOriginalDetailView(original_views.DetailView):
    def __init__(self):
        super().__init__(Document.objects.all(), DocumentSerializers, IsAuthenticated)


class DocumentStandardListView(standard_views.ListView):
    def __init__(self):
        super().__init__(Document.objects.all(), DocumentSerializers, ['id'], ['id'])


class DocumentStandardDetailView(standard_views.DetailView):
    def __init__(self):
        super().__init__(Document.objects.all(), DocumentSerializers, IsAuthenticated)


class DocumentSpecialDetailView(document_views.DetailView):
    def __init__(self):
        super().__init__(Document.objects.all(), DocumentSerializers, IsAuthenticated)


def download(request, pk):
    try:
        data = Document.objects.filter(id=pk)
        url = os.getcwd() + '/others/document/' + str(data[0].file)
        r = StreamingHttpResponse(open(url, "rb"))
        r["content_type"] = "application/octet-stream;charset=UTF-8"
        r["Content-Disposition"] = "attachment;filename=" + escape_uri_path(str(data[0].origin))
        return r
    except Exception:
        raise Http404("Download error")
