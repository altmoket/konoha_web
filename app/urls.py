
from django.urls import path

from app.views import get_name, home, listar
urlpatterns = [
    path('', home, name="Home"),
    path('your-name/', get_name, name="Your Name"),
    path('listar/', listar, name="Listar")
]
    
