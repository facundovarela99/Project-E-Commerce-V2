from django.shortcuts import render
from datetime import datetime, date, timedelta
from django.contrib.auth.views import LoginView
from .forms import AuthenticationForm,CustomAuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponse


def index(request):
    context = {"year":2025} #test variable
    return render(request, "core/index.html", context)

def about(request):
    context = {"year":2025} #test variable
    return render(request, "core/about.html", context)

def products(request):
    context = {'year':2025}
    return render(request, "core/products.html", context)

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    next_page = reverse_lazy('core:index')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        user = form.get_user()
        messages.success(self.request, f'Successful login. Welcome {user.username}')
        return super().form_valid(form)