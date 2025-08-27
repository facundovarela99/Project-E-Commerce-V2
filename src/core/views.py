from django.shortcuts import render
from datetime import datetime, date, timedelta
from django.contrib.auth.views import LoginView
from .forms import AuthenticationForm,CustomAuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.models import User



def index(request):
    context = {"year":2025} #test variable
    return render(request, "core/main_templates/index.html", context)

def about(request):
    context = {"year":2025} #test variable
    return render(request, "core/main_templates/about.html", context)

def products(request):
    context = {'year':2025}
    return render(request, "core/main_templates/products.html", context)

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/main_templates/login.html'
    next_page = reverse_lazy('core:index')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        user = form.get_user()
        messages.success(self.request, f'Successful login. Welcome {user.username}')
        return super().form_valid(form)
    
class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "core/main_templates/register_user_admin.html"
    success_url = reverse_lazy("core:login")

    def form_valid(self, form: CustomUserCreationForm) -> HttpResponse:
        messages.success(self.request, f'Successful registration. You can log in now.')
        return super().form_valid(form)