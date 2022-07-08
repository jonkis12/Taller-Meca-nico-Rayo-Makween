from email import message
from django.shortcuts import render, redirect

from core.forms import ContactoForm, TrabajoForm, CustomUserCreationForm
from .models import Contacto, Trabajo
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    
    return render(request, 'core/index.html')


def form_cliente(request):
    datos = {
        'form': ContactoForm()
    }
    
    if request.method=='POST':
        formulario=ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Datos guardados correctamente'
    
    return render(request, 'core/form_cliente.html', datos)

def perfil_usuario(request,):
    
    contacto = Contacto.objects.all()
    
    
    datos = {
        
        'contactos': contacto
    }
    
    return render(request, 'core/perfil_cliente.html', datos)

def login_admin(request):
    
    return render(request, 'core/login_admin.html')

def index2(request):
    
    return render(request, 'core/index2.html')

def apro_form(request):
    contactos = Contacto.objects.all()
    trabajo = Trabajo.objects.all()
    datos ={
        'contactos': contactos,
        'trabajos': trabajo
    }
    

    return render(request, 'core/apro_form.html', datos)

def forms(request):
    
    contactos = Contacto.objects.all()
    datos ={
        'contactos': contactos
    }
    
    return render(request, 'core/forms.html', datos)

def form_mod(request, id):
    
    contacto = Contacto.objects.get(rut=id)
    
    datos = {
        
        'form': ContactoForm(instance=contacto)
    }
    
    if request.method=='POST':
        formulario=ContactoForm(data=request.POST, instance=contacto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Datos modificados correctamente'
    
    return render(request, 'core/form_mod.html', datos)

def form_del(request, id):
    contacto = Contacto.objects.get(rut=id)
    contacto.delete()
    return redirect(to="home")

def form_del2(request, id):
    trabajo = Trabajo.objects.get(id=id)
    trabajo.delete()
    return redirect(to="apro_form")


def apro_trabajo(request):
    datos = {
        'form': TrabajoForm()
    }
    if request.method=='POST':
        formulario=TrabajoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Datos guardados correctamente'
    
    return render(request, 'core/apro_trabajo.html', datos)


def trabajo_mod(request, id):
    trabajo = Trabajo.objects.get(id=id)
    datos = {
        
        'form': TrabajoForm(instance=trabajo)
    }
    
    if request.method=='POST':
        formulario=TrabajoForm(data=request.POST, instance=Trabajo.objects.get(id=id))
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Datos modificados correctamente'
    
    return render(request, 'core/trabajo_mod.html', datos)

def trabajos(request):
    
    trabajo = Trabajo.objects.all()
    datos ={
        'trabajos': trabajo
    }
    
    
    return render(request, 'core/trabajos.html', datos)


def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
       
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)
