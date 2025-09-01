from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'product/index.html')

def category_list(request):
    categories = models.Category.objects.all()
    return render(request, 'product/category_list.html', {'categories':categories})