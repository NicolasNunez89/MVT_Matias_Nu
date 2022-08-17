# Create your views here.
from datetime import datetime
import numbers
from time import time
#from os import listxattr
from django.http import HttpResponse
from django.shortcuts import render , HttpResponse
from AppMVT.forms import Familiar

def carga_familiar(request):
    
    if request.method == "POST":
        miFormulario = Familiar(request.POST,request.user)
        print(miFormulario)
        
        if miFormulario.is_valid:
            infor=miFormulario.cleaned_data
            familia=Familiar(Nombre=infor["Nombre"], Edad=infor["Edad"], Fecha=infor["Fecha"])
            print(familia)
            familia.save()
            #infor=miFormulario.cleaned_data
            return render(request)
    else:
        miFormulario=Familiar()
    
    return render(request, "template.html", {"miFormulario": miFormulario})