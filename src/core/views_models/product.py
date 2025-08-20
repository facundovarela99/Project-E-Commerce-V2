from ..models import Product
from ..forms import ProductForm


from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('core:product_list')

# class ProductDeleteView(DeleteView):
#     model = Product

# class ProductDetail(DetailView):
#     model = Product

# class ProductUpdate(UpdateView):
#     model = Product