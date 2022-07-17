from django.db import models

from api.models.Tecnica import Tecnica
class TecnicaAtaque(Tecnica):
    rango_ataque = models.IntegerField(default=0)
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.elemento
        yield self.es_oculta
        yield self.cantidad_chakra
        yield self.rango_ataque
    def add_values(self, values):
        headers = TecnicaAtaque.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'Elemento':
                self.edad = values[i]
            elif headers[i] == 'Es Oculta':
                self.sexo = values[i]
            elif headers[i] == 'Cantidad Chakra':
                self.clan = values[i]
            elif headers[i] == 'Rango Ataque':
                self.rango_ataque = values[i]
    @staticmethod
    def get_headers():
        headers = Tecnica.get_headers()
        headers.append("Rango Ataque")
        return headers
    @staticmethod
    def get_types():
        types = Tecnica.get_types()
        types.append('Int')
        return types
    @staticmethod
    def get_pointers():
        pointers = Tecnica.get_pointers()
        pointers.append('')
        return pointers
