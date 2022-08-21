from django.urls import path
from AppMVT import views


urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
<<<<<<< HEAD
    path('carga_familiar/', views.carga_familiar, name="carga_familiar"),
    path('mostrar_Familiar/', views.mostrar,name="mostrar"),
=======
    path('carga_familiar/', views.carga_familiar, name="carga_familiar")
>>>>>>> 5a0dfdb3cf6eff1b0cb48d8ea7e464bd9f7ca99a
]