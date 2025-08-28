from ..models import Product
from ..forms import ProductForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

#-----------Class-based Views-----------
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'core/product_crud/product_list.html'

    def get_queryset(self): #Busqueda filtrada en vista basada en clase
        search = self.request.GET.get('busqueda')
        if search:
            queryset =  Product.objects.filter(name__icontains=search)
        else:
            queryset = super().get_queryset() #Se ejecuta método de la clase padre (que por defecto trae todos los objetos)
            # queryset = Product.objects.all() (Puede ser una u otra opción)
        return queryset
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/product_crud/product_form.html'
    success_url = reverse_lazy('core:product_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/product_crud/product_form.html'
    success_url = reverse_lazy('core:product_list')

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'core/product_crud/product_detail.html'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'core/product_crud/product_list.html'
    success_url = reverse_lazy('core:product_list')

