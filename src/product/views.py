from django.shortcuts import render, redirect
from . import models, forms

context = {"year":2025}

def index(request):
    return render(request, 'product/index.html', context)

def category_list(request):
    categories = models.Category.objects.all()
    context2 = context.copy()
    context2.update({"categories":categories})
    return render(request, 'product/category_list.html', context2)

def category_create(request):
    if request.method == 'GET':
        form = forms.CategoryForm
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST) #Se crea una instancia de formulario que tendrá los datos que el usuario envió
        if form.is_valid():
            form.save()
            return redirect('product:category_list')
    context2 = context.copy()
    context2.update({'form':form})
    return render(request, 'product/category_form.html', context2)