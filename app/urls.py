
from django.urls import path

from app.views import home, listar, agregar, agregar_elemento, eliminar_elemento, editar, editar_elemento
urlpatterns = [
    path('', home, name="Home"),
    path('listar/', listar, name="listar"),
    path('editar/<str:data>/<int:pk>', editar, name="editar"),
    path('agregar/<str:data>', agregar, name="agregar"),
    path('agregar/', agregar_elemento, name="agregar elemento"),
    path('editar/', editar_elemento, name="editar elemento"),
    path('eliminar/<str:data>/<int:pk>', eliminar_elemento, name="eliminar elemento")
]
    
