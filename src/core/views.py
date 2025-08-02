from django.shortcuts import render
from django.http import HttpResponse

#TEST FUNCTIONS
# def greet(request):
#     return HttpResponse("Hello from Django!")

# def greet_with_label(request):
#     return HttpResponse("<h1>App tittle</h1>")

# def greet_with_parameters(request, name: str, last_name: str):
#     name = name.capitalize()
#     last_name = last_name.capitalize()
#     return HttpResponse(f"{last_name}, {name}")

def index(request):
    context = {"year":2025} #test variable
    return render(request, "core/index.html", context)