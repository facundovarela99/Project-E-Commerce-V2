from ..models import Product
from ..forms import ProductForm


from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

#-----------Class-based Views-----------
class ProductListView(ListView):
    model = Product

    def get_queryset(self): #Busqueda filtrada en vista basada en clase
        search = self.request.GET.get('busqueda')
        if search:
            queryset =  Product.objects.filter(name__icontains=search)
        else:
            queryset = super().get_queryset() #Se ejecuta método de la clase padre (que por defecto trae todos los objetos)
            # queryset = Product.objects.all() (Puede ser una u otra opción)
        return queryset
    
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('core:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('core:product_list')

class ProductDetail(DetailView):
    model = Product

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('core:product_list')

