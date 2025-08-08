from django.shortcuts import render
from django.http import HttpResponse
from .models import Client

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

def roll_dice(request):
    from datetime import datetime
    from random import randint

    dice_roll = randint(1, 6)
    if dice_roll == 6:
        message = f"You had thrown the dice and you haven taken out ¡{dice_roll}! You won!"
    else:
        message = f"You had thrown the dice and you haven taken out ¡{dice_roll}! Keep trying. Press F5"

    data = {
        'title': 'Roll dice',
        'message': message,
        'date': datetime.now(),
        'year':2025
    }
    return render(request, 'core/roll_dice.html', context=data)


def calcular_edad(request):
    from datetime import datetime, date, timedelta
    nombre = "Facundo"
    apellido = "Varela"
    fecha_actual = datetime.now()
    fecha_str = "1999/04/01"
    fecha = datetime.strptime(fecha_str, '%Y/%m/%d')
    fecha_str = fecha.strftime('%d-%m-%Y')
    user_days = fecha_actual-fecha
    user_days = user_days.days
    years = user_days//365

    data = {
        'nombre':nombre,
        'apellido':apellido,
        'fecha_nacimiento':fecha_str,
        'fecha_actual':fecha_actual,
        'edad':years,
        'year':2025,
    }

    return render(request, 'core/usuario.html', context=data)

def see_clients(request):
    clients = Client.objects.all()
    return render(request, "core/index.html", {'clients':clients})