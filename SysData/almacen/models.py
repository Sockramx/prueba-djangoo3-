from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Empleado(User):
	puesto = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.puesto

class Categoria(models.Model):
	categoria = models.CharField(max_length=50, blank=True, null=True)
	descripcion = models.CharField(max_length=180, blank=True, null=True)
	
	def __str__(self):
		return self.categoria
		
class Proveedor(models.Model):
	proveedor = models.CharField(max_length=80, blank=True, null=True)
	contacto = models.CharField(max_length=100, blank=True, null=True)
	telefono = models.CharField(max_length=10, blank=True, null=True)
	celular = models.CharField(max_length=10, blank=True, null=True)
	
	def __str__(self):
		return self.proveedor

class Producto(models.Model):
	producto = models.CharField(max_length=50, blank=True, null=True)
	descripcion = models.CharField(max_length=180, blank=True, null=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete= models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.producto
		



# extender el modelo user 
#https://www.youtube.com/watch?v=TWYPq_AGVjQ