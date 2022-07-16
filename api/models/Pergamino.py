from django.db import models
from datetime import date
from api.models.Ninja import Ninja
from api.models.Tecnica import Tecnica
class Pergamino(models.Model):
    ninja = models.ForeignKey(Ninja, on_delete=models.CASCADE, null=False)
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, null=False)
    fecha_sellado = models.DateField(default=date(1,1,1))
    @staticmethod
    def get_headers():
        headers = ['ID', 'ID Ninja', 'ID Tecnica', 'Fecha Sellado']
        return headers
