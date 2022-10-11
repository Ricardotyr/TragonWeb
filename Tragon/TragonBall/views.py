from django.shortcuts import render, redirect
from TragonBall.models import Cliente
from django.contrib import messages



# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

    
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

def paginaLogin(request):
    if request.method=='POST':
        try:
            detalleC=Cliente.objects.get(correo_cliente=request.POST['correo'], clave_cliente=request.POST['password'])
            print("Cliente=", detalleC)
            request.session['Email']=detalleC.correo_cliente
            return render(request, 'inicio.html')
        except Cliente.DoesNotExist as e:
            messages.success(request, 'Nombre de usuario o password no es correcto..!')
    return render(request, 'iniciarsesion.html')

def cerrarSesion(request):
    try:
        del request.session['Email']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')



