from django.urls import path
from . import views
from product.views_models import category, product, seller, sale

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
    path('product/detail/<int:pk>', product.ProductDetailView.as_view(), name='product_detail'),
    path('product/delete/<int:pk>', product.ProductDeleteView.as_view(), name='product_delete'),
]

urlpatterns+=[
    path('seller/list', seller.seller_list, name='seller_list'),
    path('seller/create', seller.seller_create, name='seller_create'),
    path('seller/update/<int:pk>', seller.seller_update, name='seller_update'),
    path('seller/detail/<int:pk>', seller.seller_detail, name='seller_detail'),
    path('seller/delete/<int:pk>', seller.seller_delete, name='seller_delete'),
]

urlpatterns+=[
    path('sale/list', sale.sale_list, name='sale_list'),
    path('sale/create', sale.sale_create, name='sale_create'),
    path('sale/update/<int:pk>', sale.sale_update, name='sale_update'),
    path('sale/detail/<int:pk>', sale.sale_detail, name='sale_detail'),
    path('sale/delete/<int:pk>', sale.sale_delete, name='sale_delete'),
]