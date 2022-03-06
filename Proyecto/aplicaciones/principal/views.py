from django.shortcuts import render, redirect
# Create your views here.


def inicio(request):
    return render(request, 'home.html')
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
