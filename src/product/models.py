from django.db import models

# Create your models here.
class Category(models.Model):
    #Products categories
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Product categories'
    
    def validate_unique(self, exclude =None):
        return super().validate_unique(exclude)