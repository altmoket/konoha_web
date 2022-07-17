from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Genin(Ninja):
    fecha_graduacion = models.DateField(default=date(1,1,1))
    valoracion = models.CharField(max_length=200, default="")
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento
        yield self.chakra_max
        yield self.sobrenombre
        yield self.fecha_graduacion
        yield self.valoracion
    @staticmethod
    def get_headers():
        headers = Ninja.get_headers()
        headers.append('Fecha Graduacion')
        headers.append('Valoracion')
        return headers
    @staticmethod
    def get_types():
        types = Ninja.get_types()
        types.append('Date')
        types.append('Char')
        return types
    @staticmethod
    def get_pointers():
        pointers = Ninja.get_pointers()
        pointers.append('')
        pointers.append('')
        return pointers

