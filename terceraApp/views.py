from django.shortcuts import render
from django.http import HttpResponse

from terceraApp.models import *

# Create your views here.

def peliculas (request):
    peli= pelicula(nombre='star wars',anio=1977 , oscar=False)
    peli.save()
    texto=f"-->Pelicula:{peli.nombre} año:{peli.anio} oscar:{peli.oscar}"
    
    
    return HttpResponse(texto)
