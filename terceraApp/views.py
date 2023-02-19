from django.shortcuts import render



from terceraApp.models import *
from .forms import *

# Create your views here.

def inicio (request):
    return render(request,'terceraApp/inicio.html')

def peliculas (request):
    mis_peliculas=pelicula.objects.all()

    if request.method == 'POST':
        mi_formulario = PeliculaFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            peli= pelicula(nombre=informacion['nombre'], anio=informacion['anio'], oscar=informacion['oscar'])
            peli.save()
            nueva_peli = {'nombre': informacion['nombre'], 'FechaDeEstreno':informacion['anio'], 'Oscar':informacion['oscar']}
            return render (request, 'terceraApp/peliculas.html',{'peliculaformulario': mi_formulario,'nueva_peli':nueva_peli,"mis_pelis":mis_peliculas })
    else:
        mi_formulario=PeliculaFormulario()

    return render(request,'terceraApp/peliculas.html', {'peliculaformulario':mi_formulario,'mis_pelis':mis_peliculas})
   

def actores (request):
    mis_actores=actor.objects.all()


    if request.method == 'POST':
        mi_formulario = ActoresFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            act= actor(nombre=informacion['nombre'], edad=informacion['edad'], oscar=informacion['oscar'])
            act.save()
            nuevo_actor={'nombre': informacion['nombre'], 'edad':informacion['edad'], 'Oscar':informacion['oscar']}
            return render (request, 'terceraApp/actores.html',{'actoresformulario': mi_formulario,'nuevo_actor':nuevo_actor,"mis_actores":mis_actores })
    else:
        mi_formulario=ActoresFormulario()
    return render(request, 'terceraApp/actores.html', {'actoresformulario':mi_formulario, 'mis_actores':mis_actores})


def directores (request):
    mis_directores = director.objects.all()

    if request.method == 'POST':
        mi_formulario = DirectoresFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            direc= director(nombre=informacion['nombre'], obras=informacion['obra'], oscar=informacion['oscar'])
            direc.save()
            nuevo_director={'nombre': informacion['nombre'], 'obras':informacion['obra'], 'Oscar':informacion['oscar']}
            return render (request, 'terceraApp/directores.html',{'directoresformulario': mi_formulario,'nuevo_director':nuevo_director,"mis_directores":mis_directores })
    else:
        mi_formulario=DirectoresFormulario()
    return render(request, 'terceraApp/directores.html',{'directoresformulario':mi_formulario, 'mis_directores':mis_directores})
      

def busqueda_pelicula(request):
    return render(request, 'terceraApp/inicio.html')

def buscar(request):
    if request.GET["fechadeestreno"]:
        FdE= request.GET["fechadeestreno"]
        resultado=pelicula.objects.filter(anio__icontains = FdE)

        return render (request, 'terceraApp/inicio.html',{'Peliculas':resultado, 'Fechadeestreno':FdE})
    else:
        respuesta='no se encontraron estrenos ese año'
    return render(request, 'terceraApp/inicio.html',{'respuesta':respuesta})

