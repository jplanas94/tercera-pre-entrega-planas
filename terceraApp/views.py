from django.shortcuts import render,redirect
from django.http import HttpResponse


from terceraApp.models import *
from .forms import *

# Create your views here.

def inicio (request):
    return render(request,'terceraApp/inicio.html')

def peliculas (request):
    return render(request,'terceraApp/peliculas.html')
   

def actores (request):
    return render(request,'terceraApp/actores.html')

def directores (request):
    return render(request,'terceraApp/directores.html')   

def peliculas_formulario(request):

    if request.method == 'POST':
        mi_formulario = PeliculaFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            peli= pelicula(nombre=informacion['nombre'], anio=informacion['anio'], oscar=informacion['oscar'])
            peli.save()
            return redirect('inicio')
    else:
        miformulario=DirectoresFormulario()
    return render(request, 'terceraApp/peliculas-formulario.html',{'peliculaformulario':miformulario})

def directores_formulario(request):

    if request.method == 'POST':
        mi_formulario = DirectoresFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            direc= director(nombre=informacion['nombre'], obras=informacion['obra'], oscar=informacion['oscar'])
            direc.save()
            return redirect('inicio')
    else:
        miformulario=DirectoresFormulario()
    return render(request, 'terceraApp/directores-formulario.html',{'directoresformulario':miformulario})

def actores_formulario(request):

    if request.method == 'POST':
        mi_formulario = ActoresFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            act= actor(nombre=informacion['nombre'], edad=informacion['edad'], oscar=informacion['oscar'])
            act.save()
            return redirect('inicio')
    else:
        miformulario=ActoresFormulario()
    return render(request, 'terceraApp/actores-formulario.html', {'actoresformulario':miformulario})




