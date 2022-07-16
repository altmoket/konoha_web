from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Genin(Ninja):
    fecha_graduacion = models.DateField(default=date(1,1,1))
    valoracion = models.CharField(max_length=200, default="")
    @staticmethod
    def get_headers():
        headers = Ninja.get_headers()
        headers.append('Fecha Graduacion')
        headers.append('Valoracion')
        return headers

