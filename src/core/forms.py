from django import forms
from core import models

#Crear clase para el formulario
#La clase crea los campos del modelo segun sus entidades
class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"

    # def clean_name(self):
    #     name = self.cleaned_data.get('name', '')
    #     if len(name) < 3:
    #         raise 