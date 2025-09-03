from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/list', views.category_list, name='category_list'),
    path('category/create', views.category_create, name='category_create'),
    path('category/update/<int:pk>', views.category_update, name='category_update'),
    path('category/detail/<int:pk>', views.category_detail, name='category_detail'),
    path('category/delete/<int:pk>', views.category_delete, name='category_delete'),
]