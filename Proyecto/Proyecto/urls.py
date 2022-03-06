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
from aplicaciones.principal.views import inicio, my_view, login, inicio_c
from aplicaciones.principal.class_view import ClienteUpdate
# from aplicaciones.principal.class_view import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', inicio, name='home'),
    path('login/', login, name='login'),
    path('home/cliente/<int:pk>/', inicio_c, name='home_l'),
    # path('crear_persona/', PersonaCreate.as_view(), name='crear_persona'),
    # path('editar_persona/<int:pk>/', PersonaUpdate.as_view(), name="editar_persona"),
    # path('eliminar_persona/<int:pk>/', PersonaDelete.as_view(), name="eliminar_persona"),
]

urlpatterns += staticfiles_urlpatterns()