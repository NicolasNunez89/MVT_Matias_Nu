from django import forms

# Create your models here.

class CargaFamiliar(forms.Form):
    Nombre = forms.CharField(max_length=30)
    Edad = forms.IntegerField()
    Fecha = forms.DateField()