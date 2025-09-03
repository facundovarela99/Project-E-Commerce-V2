from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .. import models, forms

context = {"year":2025}

# --------------PRODUCT - LIST VIEW--------------CLASS-BASED VIEW
class ProductListView(ListView):
    model = models.Product
    template_name = 'product/Product_crud/product_list.html'