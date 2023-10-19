from django.db import models
from django.conf import settings



class Ropa(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    talla = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    imagen = models.ImageField(upload_to='media/ropa/')  
     # Campo para relacionar la prenda de ropa con el usuariomanage.py makemigrations
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

