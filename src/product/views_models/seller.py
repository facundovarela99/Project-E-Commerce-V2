from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .. import models, forms

context = {"year":2025}

# -------SELLER - LIST VIEW-------FUNCTION-BASED VIEW
def seller_list(request: HttpRequest) -> HttpResponse:
    search = request.GET.get('search')
    if search:
        queryset = models.Seller.objects.filter(user__icontains=request.GET.get('query'))
    else:
        queryset = models.Seller.objects.all()
    context2 = context.copy()
    context2.update({"object_list":queryset})
    return render(request, 'product/Seller_crud/seller_list.html', context2)


# -------SELLER - CREATE VIEW-------FUNCTION-BASED VIEW
def seller_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = forms.SellerForm
    if request.method == 'POST':
        form = forms.SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:seller_list')
    context2 = context.copy()
    context2.update({'form':form})
    return render(request, 'product/Seller_crud/seller_form.html', context2)
