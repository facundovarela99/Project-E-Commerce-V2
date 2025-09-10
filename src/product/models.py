from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction


# Create your models here.
class Category(models.Model):
    #Products categories
    #models.UUIDField: PENDIENTE - UTILIZAR CAMPO PARA GENERAR CÓDIGO ÚNICO EN REEMPLAZO DE LA PK EN EL FRONT
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Product categories'
    
    def validate_unique(self, exclude =None):
        return super().validate_unique(exclude)
    
    def get_absolute_url(self):
        pass
    #Representa la instancia - utilizar para reemplazar el envío de la primary key por el Front

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='category')
    name = models.CharField(max_length=150, db_index=True) #facilita la búsqueda en la BD
    description = models.TextField(blank=True, null=True, verbose_name='Description') #blank: el campo puede dejarse vacío cuando es True
    # img = models.ImageField(blank=True, null=True, verbose_name='productImage')Pendiente agregar imagenes
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        base = f'{self.name} - ${self.price}'
        if self.category:
            return f'{self.category} - {base}'
        return base
    
    class Meta: #Se utiliza para definir opciones de configuración adicionales de un modelo
        unique_together = ('category', 'name') #la combinación de los campos debe ser única en la BD
        verbose_name = 'Product' #Define el nombre singular legible del modelo (también usado en el panel de ADMIN)
        verbose_name_plural = 'Products' #Define el nombre plurar legible del modelo (también usado en el panel de ADMIN)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller")
    cellphone = models.CharField(max_length=50)
    user_img = models.ImageField(upload_to="profile_images", null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    sell_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-sell_date",)
    
    # def clean(self): ACTUALEMNTE EN forms.py: clean_amount()
    #     if self.amount > self.product.stock:
    #         raise ValidationError("The amount cannot be greater than stock")
    
    def __str__(self):
        return f"{self.seller.user.username} - {self.product.name} - ${self.total_price}"


    # def substract_stock(self):
    #     self.product.stock -= self.amount
    #     self.product.save()

    # @transaction.atomic
    # def save(self, *args, **kwargs):
    #     #calcula el precio
    #     self.total_price = self.product.price * self.amount
    #     #valida antes de guardar
    #     self.full_clean()
    #     #guarda la venta
    #     super().save(*args, **kwargs)
    #     #se resta el stock despues
    #     self.substract_stock()

    # def __str__(self):
    #     return f"{self.seller.user.username} - {self.product.name} - ${self.total_price}"