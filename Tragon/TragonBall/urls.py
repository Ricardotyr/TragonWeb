from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('registrarse', views.registroCliente, name="reg"),
    path('iniciarsesion', views.paginaLogin, name='paginaLogin'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),
]