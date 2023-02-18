from django.urls import path
from .views import *
from tercerapreentrega.views import saludo,segundavista,probandotemplate


urlpatterns = [
    #path('saludo/', saludo),
    #path('segundavista/', segundavista),
    path('probandotemplate/', probandotemplate),
    path('', inicio),
    path('actores/', actores),
    path('directores/', directores),
    path('peliculas/', peliculas),
]
