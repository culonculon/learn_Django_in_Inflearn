from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("index.html")  # 이거는 직접 보내는것
    qs = Post.objects.all()
    return render(request, 'app/index.html', {'post_list': qs})
    # return render(request, 'test.html') # 서로 다름

