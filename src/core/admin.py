from django.contrib import admin

# Register your models here.
from .models import Client, Country, User

# admin.site.register(Client)
# admin.site.register(Country)
# Registro de modelos para la administración desde las vistas de admin 

@admin.register(Country) #Me permite agregar un buscador y buscar un tipo de objeto por caracteres
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Client) #Me permite agregar un buscador y buscar un tipo de objeto por caracteres
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "birth_date", "country_of_origin",)
    search_fields = ('name', 'last_name',)
    ordering = ('last_name','name',)
    list_filter = ('country_of_origin',)
    date_hierarchy = 'birth_date'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "name", "last_name", "birth_date", "country_of_origin",)
    search_fields = ('name', 'last_name','user_name')