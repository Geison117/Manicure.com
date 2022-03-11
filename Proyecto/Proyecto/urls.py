"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from aplicaciones.principal.views import *
from aplicaciones.principal.class_view import Login, logoutUsuario
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

# from aplicaciones.principal.class_view import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name = 'index'),
    #path('home/', inicio, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('agendar_cita/', agendar_cita, name='agendar_cita'),
    path('agendar_cita_seleccionada/<int:id_servicio>/', agendar_cita_seleccionada , name='agendar_cita_seleccionada'),
    path('perfil/', mostrar_perfil, name='perfil'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)