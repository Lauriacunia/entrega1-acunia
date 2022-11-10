from django.contrib import admin
from django.urls import path
from user.views import SettingsUser

urlpatterns = [
    path('/settings', SettingsUser.as_view(), name='settings'),
]