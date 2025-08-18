from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from ..models import Client, Country, User
from core import forms, models #se importa forms y se utiliza en register
from ..forms import UserForm
from ..models import User




# ***** USERS - LIST VIEW
def users_list(request: HttpRequest) -> HttpResponse: #metodo para devolver una lista de usuarios creados
    queryset = User.objects.all()
    context = {"year":2025,
               'object_list':queryset
               }
    return render(request, 'core/users_list.html', context)

# ***** USERS - CREATE VIEW
def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:register')
    return render(request, 'core/register.html', {'form':form})

def products(request):
    context = {'year':2025}
    return render(request, "core/products.html", context)

# ***** USERS - UPDATE VIEW
def update_user(request: HttpRequest, pk: int) -> HttpResponse:
    query = User.objects.get(id=pk)
    if request.method == 'GET':
        form = UserForm(instance=query)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('core:register')
    return render(request, 'core/register.html', {'form':form})

# ***** USERS - DETAIL VIEW
def user_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = User.objects.get(id=pk)
    return render(request, 'core/user_detail.html', {'object': query})


# ***** USERS - DELETE VIEW
def user_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = User.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('core:users_list')
    return render(request, 'core/user_delete_confirm.html', {'object': query})