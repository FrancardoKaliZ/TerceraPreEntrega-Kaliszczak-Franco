from django.db import models

class Comercio(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    numeroUbicacion = models.IntegerField()


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_contratacion = models.DateField()
    dni = models.CharField(max_length=100)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
