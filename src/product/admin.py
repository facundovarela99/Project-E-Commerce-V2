from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category) #Me permite agregar un buscador y buscar un tipo de objeto por caracteres

