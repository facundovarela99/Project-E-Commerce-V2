from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# class Country(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     def __str__(self):
#         return self.name
    
#Pendiente class States

#Pendiente class Cities

# class Client(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     birth_date = models.DateField(null=True, blank=True)
#     country_of_origin = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
#     def __str__(self):
#         return f'{self.name}, {self.last_name}'
    
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     user_name = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=30)
#     birth_date = models.DateField()
#     email = models.CharField(max_length=100, unique=True)
#     country_of_origin = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
#     def __str__(self):
#         return f'{self.name} - {self.last_name} - {self.user_name}'

#PENDIENTE PARA VER: https://www.bing.com/videos/riverview/relatedvideo?q=django+delete+migrations&mid=C2E591B3AD7EB9A01F29C2E591B3AD7EB9A01F29&FORM=VAMTRV
#PLAYGROUND INTERMEDIO PARTE 2: 1:53:28
# class Category(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     description = models.TextField(blank=True, null=True, verbose_name='Description')

#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = 'Product categories'
    
#     def validate_unique(self, exclude =None):
#         return super().validate_unique(exclude)

# #Created product model as a starting point to implement Class-based views (Go to core/view_models/product.py)
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=300)
#     stock = models.IntegerField(null=False)
#     def __str__(self):
#         return f'{self.name} - {self.description}'
    

# class Seller(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')