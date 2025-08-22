from django import forms
from .models import User, Product
from django.contrib.auth.forms import AuthenticationForm

#Crear clase para el formulario
#La clase crea los campos del modelo segun sus entidades

#Función para validar si el nombre contiene caracteres alfabéticos
def validate_name(name: str): 
    if not name.isalpha():
        raise forms.ValidationError('It must contain alphabetical characters')
    return name

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def clean_name(self):
        name: str = self.cleaned_data.get('name', '')
        return validate_name(name)

#Created product model as a starting point to implement Class-based views (Go to core/view_models/product.py)
#Creado modelo producto como punto de partida para implementar vistas basadas en clases(Ir a core/view_models/product.py)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =  ['name', 'description', 'stock']

    # def clean_name(self):
    #     name: str = self.cleaned_data.get('name', '')
    #     return validate_name(name)


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']
