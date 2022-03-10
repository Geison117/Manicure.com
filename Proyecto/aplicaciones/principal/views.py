
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
        if form.is_valid():
            for f in form.fields.items():
                print(f)
            form.save()
            return redirect('index')

    return render(request, 'agendar_cita.html', contexto)


