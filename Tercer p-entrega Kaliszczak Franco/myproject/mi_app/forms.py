from django import forms
from .models import Comercio, Empleado, Proyecto

class ComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = ['nombre', 'ubicacion', 'numeroUbicacion']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'edad', 'fecha_contratacion', 'dni']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']
