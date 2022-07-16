from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Jounin(Ninja):
    fecha_examen = models.DateField(default=date(1,1,1))
    calificacion_examen = models.CharField(max_length=100, default="")
    @staticmethod
    def get_headers():
        headers = Ninja.get_headers()
        headers.append("Fecha Examen")
        headers.append("Calificacion Examen")
        return headers
