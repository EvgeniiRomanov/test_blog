import datetime

from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

# Create your views here.
class SimpleView(View):
    def get(self, request: HttpRequest):
        html = f"{datetime.datetime.now()}"

        return HttpResponse(html)

class SimpleViewPost(View):
    def post(self, request: HttpRequest):
        pass
        # html = f"{datetime.datetime.now()}"

        # return HttpResponse(html)