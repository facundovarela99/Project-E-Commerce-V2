from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    country_of_origin = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.name}, {self.last_name}'
    
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.CharField(max_length=100)
    country_of_origin = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.name}, {self.last_name}'