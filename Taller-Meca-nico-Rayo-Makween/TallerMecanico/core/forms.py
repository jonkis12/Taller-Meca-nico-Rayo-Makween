from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Contacto
from .models import Trabajo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['rut','nombre','correo','mensaje','categoria']
        
        

class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = ['diagnostico', 'mecanico', 'fecha', 'materiales', 'img', 'categoria']


class CustomUserCreationForm(UserCreationForm):
     
     class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        