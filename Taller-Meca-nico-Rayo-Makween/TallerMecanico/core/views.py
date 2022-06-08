from django.shortcuts import render, redirect

from core.forms import ContactoForm, TrabajoForm
from .models import Contacto, Trabajo

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
    datos ={
        'contactos': contactos
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




def apro_trabajo(request):
    datos = {
        'form': TrabajoForm()
    }
    
    if request.method=='POST':
        formulario=TrabajoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Datos guardados correctamente'
    
    return render(request, 'core/apro_trabajo.html', datos)



def form_trabajo(request,):
    
    trabajo = Trabajo.objects.all()
    
    datos = {
        
        'trabajo': trabajo
    }
    
    return render(request, 'core/apro_trabajo.html', datos)