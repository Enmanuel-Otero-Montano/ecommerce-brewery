from os import access
from django.shortcuts import render
from django.core.mail import EmailMessage
from Proyecto_Final_de_BIOS_Python import settings
from cerveceria.models import Cerveza
from cerveceria.forms import ContactoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string


# Create your views here.

def inicio(request):
    beer = Cerveza.objects.order_by("stock")[:3]
    return render(request, 'index.html', {"cervezas": beer})

def contacto(request):
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            subject = formulario.cleaned_data["asunto"]
            message = formulario.cleaned_data["mensaje"]
            email_from = 'Enviado por {}'.format(formulario.cleaned_data["correo_electrónico"])
            email_to = ["oteromontanoenmanuel@gmail.com"]

            template = render_to_string("email-sent.html", {
                "email_from": email_from,
                "message": message
            })

            email = EmailMessage(subject, template, settings.EMAIL_HOST_USER, email_to)

            email.send()
            return render(request, 'correo-enviado.html')
        else:
            return render(request, 'correo-no-enviado.html')
    else:
        formulario = ContactoForm()
        return render(request, 'contacto.html', {"formulario": formulario})

def sobre_nosotros(request):
    return render(request, 'sobre-nosotros.html') 

def buscar_cerveza(request):
    if "search-beer" in request.GET:
        search = request.GET["search-beer"]
        beer = Cerveza.objects.filter(marca__contains = search)
        return render(request, 'resultados-busqueda.html', {"cervezas": beer})
    else:
        return render(request, 'resultados-busqueda.html')

def nuestros_productos(request):
    productos = Cerveza.objects.all()
    return render(request, 'nuestros-productos.html', {"productos": productos})

def new_user(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        try:
            formulario.save()
            return render(request, 'usuario-agregado.html')
        except:
            return render(request, 'usuario-nuevo.html', {"formulario": formulario})  
    else:
        formulario = UserCreationForm()
        return render(request, 'usuario-nuevo.html', {"formulario": formulario})

def ingresar(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('/privado')
    elif request.method == "POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST["username"]
            password = request.POST["password"]
            access = authenticate(username = user, password = password) 
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/privado')
            else:
                return render(request, 'no-usuario.html')
    else:
        formulario = AuthenticationForm()
        return render(request, 'ingresar.html', {"formulario": formulario})

@login_required(login_url = '/ingresar')
def privado(request):
    user = request.user
    return render(request, 'privado.html', {"usuario": user})

def salir(request):
    if not request.user.is_anonymous:
        logout(request)
        return HttpResponseRedirect('/ingresar')

def page_not_found(request, exception):
    return render(request, 'page-not-found.html', {})

def error_500(request):
    return render(request, 'page-error-500.html', {})


