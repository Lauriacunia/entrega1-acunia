from django.shortcuts import render
from post.models import Post
# Create your views here.

def showHome(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})