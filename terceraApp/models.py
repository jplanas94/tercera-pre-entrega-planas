from django.db import models

# Create your models here.
class pelicula(models.Model):
    nombre= models.CharField(max_length=40)
    anio= models.IntegerField()
    oscar= models.BooleanField()

class actor(models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    oscar= models.BooleanField()

class director(models.Model):
    nombre= models.CharField(max_length=40)
    peliculas= models.CharField(max_length=40)
    oscar= models.BooleanField()