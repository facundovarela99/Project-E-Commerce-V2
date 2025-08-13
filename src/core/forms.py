from django import forms
from core import models

#Crear clase para el formulario
#La clase crea los campos del modelo segun sus entidades
class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"
