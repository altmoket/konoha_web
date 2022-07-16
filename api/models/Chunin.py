from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Chunin(Ninja):
    fecha_examen = models.DateField(default=date(1,1,1))
    calificacion_examen = models.CharField(max_length=100, default="")
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento
        yield self.chakra_max
        yield self.sobrenombre
        yield self.fecha_examen
        yield self.calificacion_examen
    @staticmethod
    def get_headers():
        headers = Ninja.get_headers()
        headers.append('Fecha Examen')
        headers.append('Calificacion Examen')
        return headers
