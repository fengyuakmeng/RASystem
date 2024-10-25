from django.urls import path

from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("index/", IndexView.as_view(), name="index"),
    path("about/", AboutPageView.as_view(), name="about"),
]
