from django.shortcuts import render, redirect
from . import models, forms
from django.http import HttpRequest, HttpResponse

context = {"year":2025}

def index(request):
    return render(request, 'product/index.html', context)

# --------------CATEGORY - LIST VIEW--------------
def category_list(request: HttpRequest) -> HttpResponse: #anotación de tipo (HttpRequest) que devuelve una respuesta
    queryset = models.Category.objects.all()
    context2 = context.copy()
    context2.update({"object_list":queryset})
    return render(request, 'product/category_list.html', context2)

# --------------CATEGORY - CREATE VIEW--------------
def category_create(request: HttpRequest) -> HttpResponse: 
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

# --------------CATEGORY - UPDATE VIEW--------------
def category_update(request: HttpRequest, pk: int) -> HttpResponse: 
    query = models.Category.objects.get(id=pk)
    if request.method == 'GET':
        form = forms.CategoryForm(instance=query) #al entrar a la vista, muestra lo que ya se encontraba guardado
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST, instance=query) #Se crea una instancia de formulario que tendrá los datos que el usuario envió/instance: no creará un registro nuevo, se actualizará la instancia actual
        if form.is_valid():
            form.save()
            return redirect('product:category_list')
    context2 = context.copy()
    context2.update({'form':form})
    return render(request, 'product/category_form.html', context2)

# --------------CATEGORY - DETAIL VIEW--------------
def category_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Category.objects.get(id=pk)
    context2= context.copy()
    context2.update({'object':query})
    return render(request, 'product/category_detail.html', context2)