from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Country
from datetime import datetime, date, timedelta
from core import forms, models #se importa forms y se utiliza en register


def index(request):
    context = {"year":2025} #test variable
    return render(request, "core/index.html", context)

def about(request):
    context = {"year":2025} #test variable
    return render(request, "core/about.html", context)

def register(request):
    form = forms.UserForm()
    return render(request, 'core/register.html', {'form':form})