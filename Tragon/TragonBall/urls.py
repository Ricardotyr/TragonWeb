from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.paginaIndex, name="index"),
    path('registrarse', views.registroCliente, name="reg"),
    path('login', views.login, name="login"),
]