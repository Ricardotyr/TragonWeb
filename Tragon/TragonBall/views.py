from django.shortcuts import render
from TragonBall.models import Cliente
from django.contrib import messages

# Create your views here.

def paginaIndex(request):
    return render(request, 'index.html')

def registroCliente(request):
    if request.method=='POST':
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        correo= request.POST['correo']
        clave=request.POST['password']
        telefono=request.POST['telefono']
        fecha=request.POST['fecha']
        Cliente(nombre_cliente=nombre, apellido_cliente=apellido, correo_cliente=correo, clave_cliente=clave, telefono_cliente=telefono, fecharegistrocliente=fecha).save()
        messages.success(request, request.POST['nombre'] +' se registro exitosamente')
        return render(request, 'registrarse.html')
    else:
        return render(request, 'registrarse.html')