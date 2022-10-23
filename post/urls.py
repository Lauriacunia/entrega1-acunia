from django.contrib import admin
from django.urls import path
from post.views import showHome

urlpatterns = [
    path('', showHome, name='home'),
]