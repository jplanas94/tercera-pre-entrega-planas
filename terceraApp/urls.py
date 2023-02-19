from django.urls import path
from .views import *



urlpatterns = [
    path('', inicio, name='inicio'),
    path('actores/', actores, name='actores'),
    path('directores/', directores, name='directores'),
    path('peliculas/', peliculas, name='peliculas'),
    path('peliculas-formulario/', peliculas_formulario, name='peliculas-formulario'),
    path('actores-formulario/', actores_formulario, name='actores-formulario'),
    path('directores-formulario/', directores_formulario, name='directores-formulario'),
    path('busqueda-peliculas/', busqueda_peliculas, name='busqueda-peliculas'),
    path('buscar/', buscar, name='buscar'),


]
