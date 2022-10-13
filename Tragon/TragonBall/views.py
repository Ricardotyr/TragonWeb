from email.message import EmailMessage
from django.shortcuts import render, redirect
from TragonBall.models import Cliente
from django.contrib import messages
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def inicio2(request):
    return render(request, "inicio2.html")

    
def registroCliente(request):
    if request.method=='POST':
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        correo= request.POST['correo']
        clave=request.POST['password']
        telefono=request.POST['telefono']
        fecha=request.POST['fecha']
        Cliente(nombre_cliente=nombre, apellido_cliente=apellido, correo_cliente=correo, clave_cliente=clave, telefono_cliente=telefono, fecharegistrocliente=fecha).save()
        messages.success(request, request.POST['nombre'] +' se registro correctamente.')
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
            messages.success(request, 'Email o contraseña incorrecta!')
    return render(request, 'iniciarsesion.html')

def cerrarSesion(request):
    try:
        del request.session['Email']
        
    except:
        return render(request, 'inicio.html')
    return render(request, 'inicio.html')


# Contacto
def contacto(request):
    formulario=FormularioContacto()
    
    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            correo=request.POST.get("correo")
            mensaje=request.POST.get("mensaje")

            correo=EmailMessage("Mensaje desde Tragón Ball Z",
            "El usuario con nombre {} y correo {}  envia lo siguiente:\n\n {}".format(nombre,correo,mensaje),
            "",["tragonballzpyme@gmail.com"],reply_to=[correo])

            try: 
                correo.send()
                messages.success(request, 'Se ha enviado correctamente su mensaje')
                return redirect("contacto")
            except:    
                return redirect("contacto")
    return render(request, "contacto.html", {"miFormulario":formulario})