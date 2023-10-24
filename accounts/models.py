

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User




class Ropa(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    imagen = models.ImageField(upload_to='media/ropa/')  
     # Campo para relacionar la prenda de ropa con el usuariomanage.py makemigrations
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

class Zapatos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    imagen = models.ImageField(upload_to='media/zapatos/') 
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Accesorios(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    imagen = models.ImageField(upload_to='accesorios/')  
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    predeterminado = models.BooleanField(default=False)
