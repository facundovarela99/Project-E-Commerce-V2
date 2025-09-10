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
        model = models.Product
        fields = ['category','name', 'description', 'price', 'stock']
    def clean_name(self):
        name: str = self.cleaned_data.get('name', '')
        return validate_name(name)
    
class SellerForm(forms.ModelForm):
    class Meta:
         model = models.Seller
         fields = ['user', 'cellphone', 'user_img']

class SaleForm(forms.ModelForm):
    class Meta:
          model = models.Sale
          fields = ['product', 'amount']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(SaleForm, self).__init__(*args, **kwargs)
        if self.user:
             seller = models.Seller.objects.get(user=self.user)
             self.fields['seller'] = forms.CharField(initial=seller.user.username, widget=forms.TextInput(attrs={'readonly': 'readonly'}),)
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        product = self.cleaned_data.get('product')
        if amount and product and amount > product.stock:
             raise forms.ValidationError('The amount cannot be greater than stock')
        return amount