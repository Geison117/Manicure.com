
from django.shortcuts import render, redirect


from .models import Servicio


# Create your views here.


def inicio(request):
    return render(request, 'home.html')


def agendar_cita(request):
    servicios = Servicio.objects.all()  # select * from persona
    contexto = {
        'servicios': servicios
    }
    print(servicios[0].foto.url)
    return render(request, 'agendar_cita.html', contexto)