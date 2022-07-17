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
    def add_values(self, values):
        headers = Genin.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'Edad':
                self.edad = values[i]
            elif headers[i] == 'Sexo':
                self.sexo = values[i]
            elif headers[i] == 'Clan':
                self.clan = values[i]
            elif headers[i] == 'Fecha Nacimiento':
                self.fecha_nacimiento = values[i]
            elif headers[i] == 'Chakra Maximo':
                self.chakra_max = values[i]
            elif headers[i] == 'Sobrenombre':
                self.sobrenombre = values[i]
            elif headers[i] == 'Fecha Graduacion':
                self.fecha_graduacion = values[i]
            elif headers[i] == 'Valoracion':
                self.valoracion = values[i]
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

