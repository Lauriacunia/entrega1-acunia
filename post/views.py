from django.views import View 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView 
from django.shortcuts import redirect, render
from post.models import Post
from .forms.forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'base_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class CreatePost(CreateView):
    model = Post
    template_name = 'write.html'
    form_class = PostForm

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})
        
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_posts')
        return render(request, self.template_name, {'form': form})




