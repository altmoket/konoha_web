
from django.urls import path

from app.views import get_name, home, listar, agregar_view, agregar_elemento, eliminar_elemento
urlpatterns = [
    path('', home, name="Home"),
    path('your-name/', get_name, name="Your Name"),
    path('listar/', listar, name="listar"),
    path('agregar/<str:data>', agregar_view, name="agregar"),
    path('agregar/', agregar_elemento, name="agregar elemento"),
    path('eliminar/<str:data>/<int:pk>', eliminar_elemento, name="eliminar elemento")
]
    
