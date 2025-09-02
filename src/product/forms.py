from django import forms
from . import models

class CategoryForm(forms.ModelForm): #Clase que nos permite trabajar los formularios indicandole los campos del modelo (ahorra líneas en el HTML y los carga de manera determinada)
    class Meta: #subclase Meta:sirve para configurar opciones adicionales que afectan cómo se comporta ese modelo.
        model = models.Category
        fields = ['name','description']
