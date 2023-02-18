from django.http import HttpResponse
from django.template import Template, Context, loader


def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segundavista(request):
	return HttpResponse('esta esl la segunda vista')

def probandotemplate(request):
	plantilla= loader.get_template('padre.html')
	diccionario={}
	#contexto= Context()
	documento = plantilla.render(diccionario)
	return HttpResponse(documento)