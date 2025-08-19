from django.shortcuts import render
from datetime import datetime, date, timedelta

def index(request):
    context = {"year":2025} #test variable
    return render(request, "core/index.html", context)

def about(request):
    context = {"year":2025} #test variable
    return render(request, "core/about.html", context)

def products(request):
    context = {'year':2025}
    return render(request, "core/products.html", context)