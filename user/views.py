from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .forms.forms import CreateUserForm
# Create your views here.

class RegisterUser(View):
      
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')


class LoginUser(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return render(request, 'login.html')