
from django.shortcuts import render, redirect
from .models import Comercio, Empleado, Proyecto
from .forms import ComercioForm, EmpleadoForm, ProyectoForm


def inicio(request):
    return render(request,"mi_app/index.html")

def agregar_comercio(request):
    if request.method == 'POST':
        form = ComercioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_comercio')
    else:
        form = ComercioForm()
    return render(request, 'mi_app/forms/agregar_comercio.html', {'form': form})


def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'mi_app/forms/agregar_empleado.html', {'form': form})

def agregar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_proyecto')
    else:
        form = ProyectoForm()
    return render(request, 'mi_app/forms/agregar_proyecto.html', {'form': form})

def buscar_empleado(request):
    query = request.GET.get('q')  # 'q' es el parámetro de búsqueda (dni)
    empleado = None
    if query:
        empleado = Empleado.objects.filter(dni__icontains=query)  # Búsqueda insensible a mayúsculas/minúsculas
    return render(request, 'mi_app/buscar_empleado.html', {'empleado': empleado, 'query': query})