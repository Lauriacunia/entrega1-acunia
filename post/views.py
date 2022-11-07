from django.views import View 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
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



class MyPostList(ListView):
    model = Post
    template_name = 'my_account.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    #def get_queryset(self):
        #return Post.objects.filter(author=self.request.user)

class EditPost(UpdateView):
    model = Post
    template_name = 'edit.html'
    form_class = PostForm
    context_object_name = 'post'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})
        
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_posts')
        return render(request, self.template_name, {'form': form, 'post': post})
    
class DetailPost(DetailView):
    model=Post
    template_name: str = 'detail.html'