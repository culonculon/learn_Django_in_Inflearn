from django.urls import path
from . import views
from .models import *


urlpatterns = [
    path("index", views.index, name="index"),
]
