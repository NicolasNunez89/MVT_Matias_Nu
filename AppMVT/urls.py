from django.contrib import admin
from django.urls import path
from AppMVT import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('carga_familiar/', views.carga_familiar, name="carga_familiar")
]