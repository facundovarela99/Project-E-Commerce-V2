from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/list', views.category_list, name='category_list'),
    path('category/create', views.category_create, name='category_create'),
]