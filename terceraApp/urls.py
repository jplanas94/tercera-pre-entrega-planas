from django.urls import path
from .views import *
from tercerapreentrega.views import saludo,segundavista,probandotemplate


urlpatterns = [
    #path('saludo/', saludo),
    #path('segundavista/', segundavista),
    path('probandotemplate/', probandotemplate),
    path('', inicio, name='inicio'),
    path('actores/', actores, name='actores'),
    path('directores/', directores, name='directores'),
    path('peliculas/', peliculas, name='peliculas'),
]
