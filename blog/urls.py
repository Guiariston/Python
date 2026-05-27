from django.shortcuts import render, get_object_or_404
from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("", post_list, name="home"),
]