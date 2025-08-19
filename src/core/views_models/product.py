from ..models import Product
from ..forms import ProductForm

from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product

class ProductDeleteView(DeleteView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductUpdate(UpdateView):
    model = Product