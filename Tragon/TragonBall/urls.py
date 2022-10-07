from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaIndex, name="index"),
    path('registrarse', views.registroCliente, name="reg"),
    path('iniciarsesion', views.paginaLogin, name='paginaLogin'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion')
]