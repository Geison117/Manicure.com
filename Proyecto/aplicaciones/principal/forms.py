import password as password
from django import forms
from .models import *


class LoginFormC(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['correo', 'passwd']


class ClienteForm(forms.ModelForm):
     class Meta:
         model= Cliente
         fields = '__all__'

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

class Servicio_CitaForm(forms.ModelForm):
    class Meta:
        model = Servicio_Cita
        fields = '__all__'