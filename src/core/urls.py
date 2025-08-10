from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core' #nombre para llamar en las URLS de config

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
]