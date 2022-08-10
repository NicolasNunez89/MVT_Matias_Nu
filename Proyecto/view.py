from datetime import datetime
#from os import listxattr
from django.http import HttpResponse
from django.template import loader
from django.template import Template , Context
from AppMVT.models import Familiar

def carga_familiar(self):
    
    familia=Familiar(nombre="Malvina",edad=62, fecha=datetime(1959, 8,30))
    familia.save()
    diccionario= f"Nombre:  {familia.nombre}, La edad es: {familia.edad}, la fecha de nacimiento es: {familia.fecha} "
    
    plantilla= loader.get_template('template.html')
    documento = plantilla.render(diccionario) 
    
#Anyel me queda pendiente la incorporacion del template, no logro pasar los valores.
#entrego, pero mañana paso la nueva version.

    return HttpResponse(documento)