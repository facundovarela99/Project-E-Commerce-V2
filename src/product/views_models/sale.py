from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .. import models, forms

context = {'year':2025}

# -------SALE - LIST VIEW-------FUNCTION-BASED VIEW
def sale_list(request: HttpRequest) ->HttpResponse:
    search = request.GET.get('query')
    if search:
        queryset = models.Sale.objects.filter(
            seller__user__username__icontains=search
            ) | models.Sale.objects.filter(product__name__icontains=search)
    else:
        queryset = models.Sale.objects.all()
    context2 = context.copy()
    context2.update({'object_list':queryset})
    return render(request, 'product/Sale_crud/sale_list.html', context2)

# -------SALE - CREATE VIEW-------FUNCTION-BASED VIEW
def sale_create(request: HttpRequest) -> HttpResponse: #PENDIENTE: Que al generar una venta, el stock del producto vaya disminuyendo
    if request.method == 'GET':
        form = forms.SaleForm()
    if request.method == 'POST':
        form = forms.SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            product = form.cleaned_data['product']
            amount = form.cleaned_data['amount']
            sale.total_price = product.price * amount
            sale.save()
            return redirect('product:sale_list')
    context2 = context.copy()
    context2.update({'form':form})
    return render(request, 'product/Sale_crud/sale_form.html', context2)
#PENDIENTE: Que el usuario que esté logueado solo pueda crearse a sí mismo como vendedor, y solo el admin pueda administrar los vendedores

# -------SALE - UPDATE VIEW-------FUNCTION-BASED VIEW
def sale_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Sale.objects.get(id=pk)
    if request.method == 'GET':
        form = forms.SaleForm(instance=query)
    if request.method == 'POST':
        form = forms.SaleForm(request.POST, instance=query)
        if form.is_valid():
            sale = form.save(commit=False)
            product = form.cleaned_data['product']
            amount = form.cleaned_data['amount']
            sale.total_price = product.price * amount
            sale.save()
            return redirect('product:sale_list')
    context2 = context.copy()
    context2.update({'form':form})
    return render(request, 'product/Sale_crud/sale_form.html', context2)

# -------SALE - DETAIL VIEW-------FUNCTION-BASED VIEW
def sale_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Sale.objects.get(id=pk)
    context2 = context.copy()
    context2.update({'object':query})
    return render(request, 'product/Sale_crud/sale_detail.html', context2)