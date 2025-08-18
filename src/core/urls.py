from django.contrib import admin
from django.urls import path
from core.views_models import users
from . import views

app_name = 'core' #nombre para llamar en las URLS de config

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]

urlpatterns += [
    path('register', users.register, name='register'),
    path('users_list', users.users_list, name='users_list'),
    path('update_user/<int:pk>', users.update_user, name='update_user'),
    path('user_detail/<int:pk>', users.user_detail, name='user_detail'),
    path('user_delete/<int:pk>', users.user_delete, name='user_delete'),
    path('products', users.products, name='products'),
]