from django.shortcuts import render, redirect
from . import models, forms
from django.http import HttpRequest, HttpResponse

context = {"year":2025}

def index(request):
    return render(request, 'product/index.html', context)

# --------------CATEGORY - LIST VIEW--------------FUNCTION-BASED VIEW
def category_list(request: HttpRequest) -> HttpResponse: #anotación de tipo (HttpRequest) que devuelve una respuesta
    queryset = models.Category.objects.all() #Se llama a todos los registros de la base de datos (puede paginarse/filtrarse a demanda)
    context2 = context.copy()
    context2.update({"object_list":queryset})
    return render(request, 'product/Category_crud/category_list.html', context2)

# --------------CATEGORY - CREATE VIEW--------------FUNCTION-BASED VIEW
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
    return render(request, 'product/Category_crud/category_form.html', context2)

# --------------CATEGORY - UPDATE VIEW--------------FUNCTION-BASED VIEW
def category_update(request: HttpRequest, pk: int) -> HttpResponse: 
    query = models.Category.objects.get(id=pk) #Se realiza una consulta a la base de datos trayendo el id
    if request.method == 'GET':
        form = forms.CategoryForm(instance=query) #al entrar a la vista, muestra lo que ya se encontraba guardado, traído de la base por la consulta
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST, instance=query) #Se crea una instancia de formulario que tendrá los datos que el usuario envió/instance: no creará un registro nuevo, se actualizará la instancia actual
        if form.is_valid():
            form.save()
            return redirect('product:category_list')
    context2 = context.copy()
    context2.update({'form':form})
    return render(request, 'product/Category_crud/category_form.html', context2)

# --------------CATEGORY - DETAIL VIEW--------------FUNCTION-BASED VIEW
def category_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Category.objects.get(id=pk) #Se realiza una consulta a la base de datos trayendo el id
    context2= context.copy()
    context2.update({'object':query})
    return render(request, 'product/Category_crud/category_detail.html', context2) #se pasa la instancia al HTML

# --------------CATEGORY - DELETE VIEW--------------FUNCTION-BASED VIEW
def category_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Category.objects.get(id=pk) #Se realiza una consulta a la base de datos trayendo el id
    if request.method == 'POST':
        query.delete()
        return redirect('product:category_list')
    context2= context.copy()
    context2.update({'object':query})
    return render(request, 'product/Category_crud/category_confirm_delete.html', context2)