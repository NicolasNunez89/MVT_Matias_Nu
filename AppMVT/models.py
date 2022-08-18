from django.db import models

class Familiar(models.Model):
    Nombre = models.CharField(max_length=30)
    Edad = models.IntegerField()
    Fecha = models.DateField()
    
    def __str__(self):
        return f"Nombre: {self.Nombre} - Edad: {self.Edad} - Fecha: {self.Fecha} "