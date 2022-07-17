from django.db import models
from api.models.Persona import Persona
class Ninja(Persona):
    chakra_max = models.IntegerField(default=0)
    sobrenombre = models.CharField(max_length=50, default="")
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento
        yield self.chakra_max
        yield self.sobrenombre
    @staticmethod
    def get_headers():
        headers = Persona.get_headers()
        headers.append('Chakra Maximo')
        headers.append('Sobrenombre')
        return headers
    @staticmethod
    def get_types():
        types = Persona.get_types()
        types.append('Int')
        types.append('Char')
        return types
    @staticmethod
    def get_pointers():
        pointers = Persona.get_pointers()
        pointers.append('')
        pointers.append('')
        return pointers
