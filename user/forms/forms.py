from django import forms
from django.forms import  PasswordInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'input is-info',
                                     'placeholder': 'Username'}),
            'email': TextInput(attrs={'class': 'input is-info',
                                      'placeholder': 'Email'}),
            'password1': PasswordInput(attrs={'class': 'input is-info',
                                        'placeholder': 'Password'}),
            'password2': PasswordInput(attrs={'class': 'input is-info',
                                        'placeholder': 'Confirm Password'}),
        }