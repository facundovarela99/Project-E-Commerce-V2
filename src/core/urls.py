from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core' #nombre para llamar en las URLS de config

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('users_list', views.users_list, name='users_list'),
]