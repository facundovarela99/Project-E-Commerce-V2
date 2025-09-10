from django.shortcuts import render
# from datetime import datetime, date, timedelta
# from django.contrib.auth.views import LoginView
# from django.http import HttpRequest, HttpResponse
# from django.contrib.auth.decorators import login_required

  
# from core import models
# from .models import Category

context = {"year":2025} #test variable

# @method_decorator(login_not_required, name='dispatch')
def index(request):
    return render(request, "core/main_templates/index.html", context)

# @method_decorator(login_not_required, name='dispatch')
def about(request):
    return render(request, "core/main_templates/about.html", context)

# @method_decorator(login_not_required, name='dispatch')
def products(request):
    return render(request, "core/main_templates/products.html", context)