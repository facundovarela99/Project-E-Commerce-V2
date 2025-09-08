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
    return render(request, 'product/seller_list.html', context2)