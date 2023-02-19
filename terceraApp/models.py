from django.db import models

# Create your models here.
class pelicula(models.Model):
    nombre= models.CharField(max_length=40)
    anio= models.IntegerField()
    oscar= models.BooleanField()
    
    def __str__(self):
        return self.nombre+ '(' + str(self.anio) + ')'


class actor(models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    oscar= models.BooleanField()
    def __str__(self):
        return self.nombre
    
    class meta:
        verbose_name_plural='Actores'

class director(models.Model):
    nombre= models.CharField(max_length=40)
    obras= models.CharField(max_length=40)
    oscar= models.BooleanField()
    def __str__(self):
        return self.nombre    
    
    class meta:
        verbose_name_plural='Directores'