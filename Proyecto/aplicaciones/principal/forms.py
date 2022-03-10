
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
        #id_cliente_id = forms.IntegerField(widget=forms.HiddenInput())
        #id_servicio_id = forms.IntegerField(widget=forms.HiddenInput())
        # Definir campo como oculto
        self.fields['id_cliente'].widget = forms.HiddenInput()
        self.fields['id_servicio'].widget = forms.HiddenInput()

        #No existe instancia ni su pk, entonces est
        #if not self.instance.pk:
        #self.fields['id_cliente'].initial = args[0]
        #self.fields['id_servicio'].initial = args[1]
    class Meta:
        model = Cita
        fields = "__all__"

