from django.shortcuts import render


from terceraApp.models import *

# Create your views here.

def inicio (request):
    return render(request,'terceraApp/inicio.html')

def peliculas (request):
    return render(request,'terceraApp/peliculas.html')
   

def actores (request):
    return render(request,'terceraApp/actores.html')

def directores (request):
    return render(request,'terceraApp/directores.html')   
