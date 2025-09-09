from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .. import models, forms

context = {'year':2025}

# -------SALE - LIST VIEW-------FUNCTION-BASED VIEW
def sale_list(request: HttpRequest) ->HttpResponse:
    search = request.GET.get('query')
    if search:
        queryset = models.Sale.objects.filter(product__name__icontains=search)
    else:
        queryset = models.Sale.objects.all()
    context2 = context.copy()
    context2.update({'object_list':queryset})
    return render(request, 'product/Sale_crud/sale_list.html', context2)