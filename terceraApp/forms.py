from django import forms

class DirectoresFormulario(forms.Form):
    nombre=forms.CharField()
    obra=forms.CharField()
    oscar=forms.BooleanField()

class PeliculaFormulario(forms.Form):
    nombre= forms.CharField()
    anio= forms.IntegerField()
    oscar= forms.BooleanField()

class ActoresFormulario(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()
    oscar= forms.BooleanField()