from django.urls import path
from .views import *



urlpatterns = [
    path('', inicio, name='inicio'),
    path('actores/', actores, name='actores'),
    path('directores/', directores, name='directores'),
    path('peliculas/', peliculas, name='peliculas'),
    path('buscar/', buscar, name='buscar'),


]
