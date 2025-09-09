from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category) #Me permite agregar un buscador y buscar un tipo de objeto por caracteres

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'description', 'price', 'stock')
    list_display_links = ('name',)
    list_filter = ('category',)
    search_fields = ('category', 'name')


admin.site.register(models.Seller)

@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('seller', 'product', 'amount', 'total_price', 'sell_date')