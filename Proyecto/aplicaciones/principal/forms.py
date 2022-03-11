from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Cita


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class DateInput(forms.DateInput):
    input_type = 'date'


class CitaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)

        self.fields['id_cliente'].widget = forms.HiddenInput()
        self.fields['id_servicio'].widget = forms.HiddenInput()
        self.fields['id_personal'].label = "Personal"
        self.fields['fecha'].widget = DateInput()
        self.fields['fecha'].input_formats=['%d/%m/%Y']

    class Meta:
        model = Cita
        fields = "__all__"
