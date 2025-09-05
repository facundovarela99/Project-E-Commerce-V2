from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


# #Crear clase para el formulario
# #La clase crea los campos del modelo segun sus entidades

# #Función para validar si el nombre contiene caracteres alfabéticos
# def validate_name(name: str): 
#     if not name.isalpha():
#         raise forms.ValidationError('It must contain alphabetical characters')
#     return name

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"

#     def clean_name(self):
#         name: str = self.cleaned_data.get('name', '')
#         return validate_name(name)

# #Created product model as a starting point to implement Class-based views (Go to core/view_models/product.py)
# #Creado modelo producto como punto de partida para implementar vistas basadas en clases(Ir a core/view_models/product.py)
# # class ProductForm(forms.ModelForm):
# #     class Meta:
# #         model = Product
# #         fields =  ['name', 'description', 'stock']

#     # def clean_name(self):
#     #     name: str = self.cleaned_data.get('name', '')
#     #     return validate_name(name)

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] #campos pre-establecidos del UserCreationForm
        help_texts = {'username': ''}
    def __init__(self, *args, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']