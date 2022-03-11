
from django.shortcuts import render, redirect
from .forms import *

from .models import *


# Create your views here.


def inicio(request):
    return render(request, 'home.html')


def agendar_cita(request):
    servicios = Servicio.objects.all()  # select * from persona
    contexto = {
        'servicios': servicios
    }
    return render(request, 'servicios.html', contexto)


def agendar_cita_seleccionada(request, id_servicio):

    if request.method == 'GET':
        args = [request.user.id, id_servicio]#Servicio.objects.get(id=id_servicio)]
        form = CitaForm(initial ={'id_cliente':args[0], 'id_servicio':args[1]})

        contexto = {
            'form':form
        }

    if request.method == 'POST':
        form = CitaForm(request.POST)
        contexto = {
            'form': form
        }
        for f in form.fields.items():
            print(f)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'agendar_cita.html', contexto)


def mostrar_perfil(request):
    if request.method == 'GET':
        cliente = Cliente.objects.get(id = request.user.id)
        contexto = {
            'form': cliente
        }
    return render(request, 'mi_perfil.html', contexto)