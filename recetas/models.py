from django.db import models
from django.conf import settings

# Create your models here.
class TiposIngedientes(models.Model):
    tipo = models.CharField(max_length=200)

class Ingrediente(models.Model): 
    tipo = models.ForeignKey(TiposIngedientes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)

class Receta(models.Model): 
    titulo = models.CharField(max_length=200)
    pasos = models.TextField()
    ingreidntes = models.ManyToManyField(Ingrediente)
    precio = models.IntegerField()