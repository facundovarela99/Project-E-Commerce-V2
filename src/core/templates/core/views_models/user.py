from django.http import HttpRequest, HttpResponse
from core.forms import UserProfileForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required #Decorador que obliga al cliente ingresar con un usuario, Excepto las vistas seleccionadas
from core.forms import CustomAuthenticationForm, AuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/main_templates/login.html'
    next_page = reverse_lazy('core:index')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse: #Cuando el formulario sea valido
        user = form.get_user()
        messages.success(self.request, f'Successful login. Welcome {user.username}')
        return super().form_valid(form)
    
@method_decorator(login_not_required, name="dispatch")
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