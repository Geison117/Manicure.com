
from django.shortcuts import render, redirect
from .forms import CitaForm

from .models import Servicio


# Create your views here.


def inicio(request):
    return render(request, 'home.html')


def agendar_cita(request):
    servicios = Servicio.objects.all()  # select * from persona
    contexto = {
        'servicios': servicios
    }
    return render(request, 'servicios.html', contexto)


def agendar_cita_seleccionada(request):

    form = CitaForm()
    contexto = {
        'form':form
    }

    return render(request, 'agendar_cita.html', contexto)