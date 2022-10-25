from django.contrib import admin
from django.urls import path
from post.views import showHome, newPost

urlpatterns = [
    path('', showHome, name='home'),
    path('post/new', newPost, name='newpost'),
]