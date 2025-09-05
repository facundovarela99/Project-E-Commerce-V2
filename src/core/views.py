from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, AuthenticationForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserProfileForm
# from datetime import datetime, date, timedelta
# from django.contrib.auth.views import LoginView
# from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
# # from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_not_required
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

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/main_templates/login.html'
    next_page = reverse_lazy('core:index')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse: #Cuando el formulario sea valido
        user = form.get_user()
        messages.success(self.request, f'Successful login. Welcome {user.username}')
        return super().form_valid(form)
    
# @method_decorator(login_not_required, name='dispatch')
class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "core/main_templates/register.html"
    success_url = reverse_lazy("core:login")

    def form_valid(self, form: CustomUserCreationForm) -> HttpResponse:
        messages.success(self.request, f'Successful registration. You can log in now.')
        return super().form_valid(form)
    

class UpdateProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'core/main_templates/profile.html'
    success_url = reverse_lazy('core:index')

    def get_object(self):
        #Devuelve el usuario actual en lugar de esperar un pk
        return self.request.user