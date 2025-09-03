from django import forms
from . import models

def validate_name(name: str):
    if len(name) < 3:
            raise forms.ValidationError('The name length it must be greater than 3')
    if not name.isalpha():
            raise forms.ValidationError('The name must not contain numbers')
    return name

class CategoryForm(forms.ModelForm): #Clase que nos permite trabajar los formularios indicandole los campos del modelo (ahorra líneas en el HTML y los carga de manera determinada)
    class Meta: #subclase Meta:sirve para configurar opciones adicionales que afectan cómo se comporta ese modelo.
        model = models.Category
        fields = ['name','description']
    def clean_name(self):
        name: str = self.cleaned_data.get('name', '')
        return validate_name(name)

class ProductForm(forms.ModelForm):
    class Meta:
        models = models.Product
        fields = ['category','name', 'description', 'price', 'stock']
    def clean_name(self):
        name: str = self.cleaned_data.get('name', '')
        return validate_name(name)