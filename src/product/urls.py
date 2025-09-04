from django.urls import path
from . import views
from product.views_models import category, product

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns+=[
    path('category/list', category.category_list, name='category_list'),
    path('category/create', category.category_create, name='category_create'),
    path('category/update/<int:pk>', category.category_update, name='category_update'),
    path('category/detail/<int:pk>', category.category_detail, name='category_detail'),
    path('category/delete/<int:pk>', category.category_delete, name='category_delete'),
]

urlpatterns+=[
    path('product/list', product.ProductListView.as_view(), name='product_list'),
    path('product/create', product.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', product.ProductUpdateView.as_view(), name='product_update'),
    # path('product/detail/<int:pk>', product.category_detail, name='product_detail'),
    # path('product/delete/<int:pk>', product.category_delete, name='product_delete'),
]