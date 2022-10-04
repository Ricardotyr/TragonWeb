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

def login(request):
    if request.method=='POST':
        try:
            detalleCliente= Cliente.objects.get(correo=request.POST['correo'], pwd=request.POST['password'])
            print("Cliente=", detalleCliente)
            request.session['correo']=detalleCliente.correo
            return render(request, 'index.html')
        except Cliente.DoesNotExist as e:
            messages.success(request, 'correo o contraseña incorrecta.')
    return render(request, 'login.html')

def cerrarSesion(request):
    try:
        del request.session['correo']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')