from django import forms

# Create your models here.

class Familiar(forms.Form):
    Nombre = forms.CharField()
    Edad = forms.IntegerField()
    Fecha = forms.DateField()