from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .. import models, forms
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.urls import reverse_lazy #Funcion util en escenarios con vistas basadas en clases donde la configuración de la URL no debe ser totalmente cargada al momento de la ejecución


# SALE LIST CLASS-BASED VIEW
class SaleListView(ListView):
    model = models.Sale
    template_name = 'product/Sale_crud/sale_list.html'
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            return models.Sale.objects.filter(seller__user___username__icontains=search) | models.Sale.objects.filter(product__name__icontains=search)
        return models.Sale.objects.all()

# SALE CREATE CLASS-BASED VIEW
class SaleCreateView(CreateView):
    model = models.Sale
    form_class = forms.SaleForm
    template_name = 'product/Sale_crud/sale_form.html'
    success_url = reverse_lazy('product:sale_list')
    
    def get_form_kwargs(self) -> dict:
        #Sobrescribe el método get_form_kwargs para incluir el usuario actual en los argumentos de palabra clave del formualrio
        #Retorna:
                #dict: los argumentos de palabra clave para el formulario, incluyendo el usuario actual.

        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form) -> HttpResponse:
        #Maneja la lógica cuando el formulario es válido.
        #Se llama cuando el formulario fué validado correctamente
            #Guarda la venta sin confirmar la transacción en la BD
            #Asigna el vendedor basado en el usuario actual
            #Calcula el precio total de venta
            #Actualiza el stock del producto y guarda el producto y la venta
        sale = form.save(commit=False)
        sale.seller = models.Seller.objects.get(user=self.request.user)
        product = form.cleaned_data['product']
        amount = form.cleaned_data['amount']
        sale.total_price = product.price * amount
        product.stock -= amount
        product.save()
        sale.save()
        return super().form_valid(form)

# SALE DETAIL CLASS-BASED VIEW
class SaleDetailView(DetailView):
    model = models.Sale
    template_name = 'product/Sale_crud/sale_detail.html'

# SALE DELETE CLASS-BASED VIEW
class saleDeleteView(DeleteView):
    model = models.Sale
    template_name = 'product/Sale_crud/sale_confirm_delete.html'
    success_url=reverse_lazy('product:sale_list')



# # -------SALE - LIST VIEW-------FUNCTION-BASED VIEW
# def sale_list(request: HttpRequest) ->HttpResponse:
#     search = request.GET.get('query')
#     if search:
#         queryset = models.Sale.objects.filter(
#             seller__user__username__icontains=search
#             ) | models.Sale.objects.filter(product__name__icontains=search)
#     else:
#         queryset = models.Sale.objects.all()
#     context2 = context.copy()
#     context2.update({'object_list':queryset})
#     return render(request, 'product/Sale_crud/sale_list.html', context2)

# # -------SALE - CREATE VIEW-------FUNCTION-BASED VIEW
# def sale_create(request: HttpRequest) -> HttpResponse: #PENDIENTE: Que al generar una venta, el stock del producto vaya disminuyendo
#     if request.method == 'GET':
#         form = forms.SaleForm()
#     if request.method == 'POST':
#         form = forms.SaleForm(request.POST)
#         if form.is_valid():
#             sale = form.save(commit=False)
#             product = form.cleaned_data['product']
#             amount = form.cleaned_data['amount']
#             sale.total_price = product.price * amount
#             sale.save()
#             return redirect('product:sale_list')
#     context2 = context.copy()
#     context2.update({'form':form})
#     return render(request, 'product/Sale_crud/sale_form.html', context2)
# #PENDIENTE: Que el usuario que esté logueado solo pueda crearse a sí mismo como vendedor, y solo el admin pueda administrar los vendedores

# # -------SALE - UPDATE VIEW-------FUNCTION-BASED VIEW
# def sale_update(request: HttpRequest, pk: int) -> HttpResponse:
#     query = models.Sale.objects.get(id=pk)
#     if request.method == 'GET':
#         form = forms.SaleForm(instance=query)
#     if request.method == 'POST':
#         form = forms.SaleForm(request.POST, instance=query)
#         if form.is_valid():
#             sale = form.save(commit=False)
#             product = form.cleaned_data['product']
#             amount = form.cleaned_data['amount']
#             sale.total_price = product.price * amount
#             sale.save()
#             return redirect('product:sale_list')
#     context2 = context.copy()
#     context2.update({'form':form})
#     return render(request, 'product/Sale_crud/sale_form.html', context2)

# # -------SALE - DETAIL VIEW-------FUNCTION-BASED VIEW
# def sale_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     query = models.Sale.objects.get(id=pk)
#     context2 = context.copy()
#     context2.update({'object':query})
#     return render(request, 'product/Sale_crud/sale_detail.html', context2)

# # -------SALE - DELETE VIEW-------FUNCTION-BASED VIEW
# def sale_delete(request: HttpRequest, pk: int) -> HttpResponse:
#     query = models.Sale.objects.get(id=pk)
#     if request.method == 'POST':
#         query.delete()
#         return redirect('product:sale_list')
#     context2 = context.copy()
#     context2.update({'object':query})
#     return render(request, 'product/Sale_crud/sale_confirm_delete.html', context2)