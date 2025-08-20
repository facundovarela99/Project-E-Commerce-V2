from django.contrib import admin
from django.urls import path
from core.views_models import users, product
from . import views

app_name = 'core' #nombre para llamar en las URLS de config

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),

]

#USER URLS
urlpatterns += [
    path('register', users.register, name='register'),
    path('users_list', users.users_list, name='users_list'),
    path('update_user/<int:pk>', users.update_user, name='update_user'),
    path('user_detail/<int:pk>', users.user_detail, name='user_detail'),
    path('user_delete/<int:pk>', users.user_delete, name='user_delete'),
]

#TEST 'PRODUCT' CLASS-BASED VIEW URL
urlpatterns += [
    path('product_list', product.ProductListView.as_view(), name='product_list'),
    path('product_create', product.ProductCreateView.as_view(), name='product_create'),
    path('update_product/<int:pk>', product.ProductUpdateView.as_view(), name='update_product'),
    path('product_detail/<int:pk>', product.ProductDetail.as_view(), name='product_detail'),
    path('product_delete/<int:pk>', product.ProductDeleteView.as_view(), name='product_delete'),
]