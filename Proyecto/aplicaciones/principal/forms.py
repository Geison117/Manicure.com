
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


class CitaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)

        # Definir campo como oculto
        self.fields['id_cliente'].widget = forms.HiddenInput()

        # No existe instancia ni su pk, entonces est
        #if not self.instance.pk:
        #    self.fields['estado'].initial = 'activo'

    class Meta:
        model = Cita
        fields = '__all__'

