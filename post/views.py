from django.shortcuts import redirect, render
from post.models import Post
from .forms.forms import PostForm

# Create your views here.

def showHome(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def newPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'write.html', {'form': form})