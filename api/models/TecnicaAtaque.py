from django.db import models

from api.models.Tecnica import Tecnica
class TecnicaAtaque(Tecnica):
    rango_ataque = models.IntegerField(default=0)
    @staticmethod
    def get_headers():
        headers = Tecnica.get_headers()
        headers.append("Rango Ataque")
        return headers
