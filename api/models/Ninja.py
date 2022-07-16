from django.db import models
from api.models.Persona import Persona
class Ninja(Persona):
    chakra_max = models.IntegerField(default=0)
    sobrenombre = models.CharField(max_length=50, default="")
    @staticmethod
    def get_headers():
        headers = Persona.get_headers()
        headers.append('Chakra Maximo')
        headers.append('Sobrenombre')
        return headers
