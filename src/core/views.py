from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Country, User
from datetime import datetime, date, timedelta
from core import forms, models #se importa forms y se utiliza en register


def index(request):
    context = {"year":2025} #test variable
    return render(request, "core/index.html", context)

def about(request):
    context = {"year":2025} #test variable
    return render(request, "core/about.html", context)

def users_list(request): #metodo para devolver una lista de usuarios creados
    users = models.User.objects.all()
    return render(request, 'core/users_list.html', {'users':users})

def register(request):
    if request.method == 'GET':
        form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:register')
    return render(request, 'core/register.html', {'form':form})

def products(request):
    context = {'year':2025}
    return render(request, "core/products.html", context)