from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Country
from datetime import datetime, date, timedelta

def index(request):
    context = {"year":2025} #test variable
    return render(request, "core/index.html", context)

def register(request):
    context = {"year":2025} #test variable
    return render(request, "core/register.html", context)

def about(request):
    context = {"year":2025} #test variable
    return render(request, "core/about.html", context)