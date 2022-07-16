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
    @staticmethod
    def get_headers():
        headers = Tecnica.get_headers()
        headers.append("Rango Ataque")
        return headers
