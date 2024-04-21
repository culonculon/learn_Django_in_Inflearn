from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        """

        """
    )
