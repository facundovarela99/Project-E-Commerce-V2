from django.shortcuts import render
from . import models

context = {"year":2025}

def index(request):
    return render(request, 'product/index.html', context)

def category_list(request):
    categories = models.Category.objects.all()
    context2 = context.copy()
    context2.update({"categories":categories})
    return render(request, 'product/category_list.html', context2)