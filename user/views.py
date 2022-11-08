from django.shortcuts import render
from django.views import View

# Create your views here.

class RegisterUser(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        return render(request, 'register.html')

class LoginUser(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return render(request, 'login.html')