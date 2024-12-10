from django.urls import path
from mi_app import views

urlpatterns = [

    path("", views.inicio, name="inicio"),

    
    path('agregar_comercio/', views.agregar_comercio, name='agregar_comercio'),
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('agregar_proyecto/', views.agregar_proyecto, name='agregar_proyecto'),
    path('buscar_empleado/', views.buscar_empleado, name='buscar_empleado'),
]
