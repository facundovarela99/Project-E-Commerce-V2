from django.contrib import admin
from . import views
from django.urls import path
# from core.views_models import users, product
from django.contrib.auth.views import LogoutView
from core.templates.core.views_models import user
from django.conf import settings
from django.conf.urls.static import static #importación para indicarle la ruta de archivos de imágenes

app_name = 'core' #nombre para llamar en las URLS de config

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('register/', user.CustomRegisterView.as_view(), name='register'),
    path('login/', user.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/main_templates/logout.html'), name='logout'),
    path('profile/', user.UpdateProfileView.as_view(), name='profile'),
]

if settings.DEBUG: #Etapa de desarrollo
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)