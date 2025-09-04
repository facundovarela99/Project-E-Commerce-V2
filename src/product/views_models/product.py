from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .. import models, forms
from django.urls import reverse_lazy #Funcion util en escenarios con vistas basadas en clases donde la configuración de la URL no debe ser totalmente cargada al momento de la ejecución

context = {"year":2025}

# --------------PRODUCT - LIST VIEW--------------CLASS-BASED VIEW
class ProductListView(ListView):
    model = models.Product
    template_name = 'product/Product_crud/product_list.html'

# --------------PRODUCT - CREATE VIEW--------------CLASS-BASED VIEW
class ProductCreateView(CreateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product/Product_crud/product_form.html'
    success_url = reverse_lazy('product:product_list')

# --------------PRODUCT - UPDATE VIEW--------------CLASS-BASED VIEW
class ProductUpdateView(UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product/Product_crud/product_form.html'
    success_url = reverse_lazy('product:product_list')

# --------------PRODUCT - DETAIL VIEW--------------CLASS-BASED VIEW
class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product/Product_crud/product_detail.html'

# --------------PRODUCT - DELETE VIEW--------------CLASS-BASED VIEW
class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product/Product_crud/product_confirm_delete.html'
    success_url = reverse_lazy('product:product_list')