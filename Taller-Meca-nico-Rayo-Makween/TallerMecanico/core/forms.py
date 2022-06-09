from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Contacto
from .models import Trabajo


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['rut','nombre','correo','mensaje','categoria']
        
        

class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = ['diagnostico', 'mecanico', 'fecha', 'materiales', 'img', 'categoria']