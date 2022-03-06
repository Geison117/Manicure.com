from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView #View
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona


class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'sesion.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'sesion.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'home.html'
    success_url = reverse_lazy('index')