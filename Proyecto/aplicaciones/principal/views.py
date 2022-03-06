from aplicaciones.principal.forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import Cliente


# Create your views here.


def inicio(request):
    return render(request, 'home.html')

def inicio_c(request, pk):
    return render(request, 'home.html')

def login(request):

    if request.POST.get('user'):

        query = Cliente.objects.filter(correo=request.POST.get('user'), passwd=request.POST.get('pass'))

        if len(query) == 1:
            return redirect('/home/cliente/'+str(query[0].id))

    return render(request, 'login.html')


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("logeado")
        ...
    else:
        # Return an 'invalid login' error message.
        print("No logeado")
        ...
#
# def crearPersona(request):
#     if request.method == 'GET':
#         form = PersonaForm()
#
#     else:
#         form = PersonaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     contexto = {
#         'form': form
#     }
#     return render(request, 'cliente.html', contexto)
#
# def editarPersona(request, id):
#     persona = Persona.objects.get(id = id)
#     if request.method == "GET":
#         form = PersonaForm(instance = persona)
#     else:
#         form= PersonaForm(request.POST, instance = persona)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#     contexto = {
#         'form': form
#     }
#     return render(request, 'cliente.html', contexto)
#
# def eliminarPersona(request, id):
#     persona = Persona.objects.get(id = id)
#     persona.delete()
#     return redirect('index')
