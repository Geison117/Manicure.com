from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Personal)
admin.site.register(Servicio)
admin.site.register(Servicio_Cita)
admin.site.register(Producto)
admin.site.register(Cita)
