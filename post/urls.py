from django.contrib import admin
from django.urls import path
from post.views import PostList, CreatePost

urlpatterns = [
    path('', PostList.as_view(), name='all_posts'),
    path('new/', CreatePost.as_view(), name='new_post'),
]