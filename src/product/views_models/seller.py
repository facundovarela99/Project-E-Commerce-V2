from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .. import models, forms

context = {"year":2025}

# -------SELLER - LIST VIEW-------FUNCTION-BASED VIEW
def seller_list(request: HttpRequest) -> HttpResponse:
    search = request.GET.get('query')
    if search:
        queryset = models.Seller.objects.filter(user__username__icontains=search)
    else:
        queryset = models.Seller.objects.all()
    context2 = context.copy()
    context2.update({'object_list':queryset})
    return render(request, 'product/Seller_crud/seller_list.html', context2)


# -------SELLER - CREATE VIEW-------FUNCTION-BASED VIEW
def seller_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = forms.SellerForm()
    if request.method == 'POST':
        form = forms.SellerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product:seller_list')
    context2 = context.copy()
    context2.update({'form':form})
    return render(request, 'product/Seller_crud/seller_form.html', context2)

# -------SELLER - UPDATE VIEW-------FUNCTION-BASED VIEW
def seller_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Seller.objects.get(id=pk)
    if request.method == 'GET':
        form = forms.SellerForm(instance=query)
    if request.method == 'POST':
        form = forms.SellerForm(request.POST, request.FILES, instance=query)
        if form.is_valid():
            form.save()
            return redirect('product:seller_list')
    context2 = context.copy()
    context2.update({"form":form})
    return render(request, 'product/Seller_crud/seller_form.html', context2)

# -------SELLER - DETAIL VIEW-------FUNCTION-BASED VIEW
def seller_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Seller.objects.get(id=pk)
    context2 = context.copy()
    context2.update({'object':query})
    return render(request, 'product/Seller_crud/seller_detail.html', context2)

# -------SELLER - DELETE VIEW-------FUNCTION-BASED VIEW
def seller_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Seller.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('product:seller_list')
    context2 = context.copy()
    context2.update({'object':query})
    return render(request, 'product/Seller_crud/seller_confirm_delete.html', context2)