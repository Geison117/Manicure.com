from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView #View
from django.urls import reverse_lazy
from .forms import *
from .models import *

class ClienteList(ListView):
    model = Cliente
    template_name = 'prueba.html'

    def get_queryset(self):
        return self.model.objects.all()

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')


class PersonalList(ListView):
    model = Personal
    template_name = 'prueba.html'

    def get_queryset(self):
        return self.model.objects.all()

class PersonalCreate(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonalUpdate(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonalDelete(DeleteView):
    model = Personal
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')


class ServicioList(ListView):
    model = Servicio
    template_name = 'prueba.html'

    def get_queryset(self):
        return self.model.objects.all()

class ServicioCreate(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class ServicioUpdate(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class ServicioDelete(DeleteView):
    model = Servicio
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')


class ProductoList(ListView):
    model = Producto
    template_name = 'prueba.html'

    def get_queryset(self):
        return self.model.objects.all()

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')


class FacturaList(ListView):
    model = Factura
    template_name = 'prueba.html'

    def get_queryset(self):
        return self.model.objects.all()

class FacturaCreate(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class FacturaUpdate(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class FacturaDelete(DeleteView):
    model = Factura
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')


class CitaList(ListView):
    model = Cita
    template_name = 'prueba.html'

    def get_queryset(self):
        return self.model.objects.all()

class CitaCreate(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class CitaUpdate(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class CitaDelete(DeleteView):
    model = Cita
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')


class Servicio_CitaList(ListView):
    model = Servicio_Cita
    template_name = 'prueba.html'

    def get_queryset(self):
        return self.model.objects.all()

class Servicio_CitaCreate(CreateView):
    model = Servicio_Cita
    form_class = Servicio_CitaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class Servicio_CitaUpdate(UpdateView):
    model = Servicio_Cita
    form_class = Servicio_CitaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class Servicio_CitaDelete(DeleteView):
    model = Servicio_Cita
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')