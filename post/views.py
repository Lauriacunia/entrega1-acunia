from django.views import View 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.shortcuts import redirect, render
from candycode.settings import LOGIN_URL
from post.models import Post
from .forms.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PostList(ListView):
    model = Post
    template_name = 'base_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']



class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'write.html'
    form_class = PostForm
    login_url: 'LOGIN_URL'

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



class MyPostList(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'my_account.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    login_url: 'LOGIN_URL'

    #def get_queryset(self):
        #return Post.objects.filter(author=self.request.user)

class EditPost(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'edit.html'
    form_class = PostForm
    context_object_name = 'post'
    login_url: 'LOGIN_URL'


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