from django.shortcuts import render

context = {"year":2025}

def index(request):
    return render(request, 'product/index.html', context)

