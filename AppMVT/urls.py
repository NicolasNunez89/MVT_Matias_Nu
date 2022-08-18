from django.urls import path
from AppMVT import views


urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('carga_familiar/', views.carga_familiar, name="carga_familiar")
]