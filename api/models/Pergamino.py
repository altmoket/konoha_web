from django.db import models
from datetime import date
from api.models.Ninja import Ninja
from api.models.Tecnica import Tecnica
class Pergamino(models.Model):
    ninja = models.ForeignKey(Ninja, on_delete=models.CASCADE, null=False)
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, null=False)
    fecha_sellado = models.DateField(default=date(1,1,1))
    def __str__(self):
        return 'P(' + str(self.pk) + ')'
    def __iter__(self):
        yield self.pk
        yield self.ninja
        yield self.tecnica
        yield self.fecha_sellado
    def add_values(self, values):
        headers = Pergamino.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'ID Ninja':
                self.ninja = values[i]
            elif headers[i] == 'ID Tecnica':
                self.tecnica = values[i]
            elif headers[i] == 'Fecha Sellado':
                self.fecha_sellado = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID', 'ID Ninja', 'ID Tecnica', 'Fecha Sellado']
        return headers
    @staticmethod
    def get_types():
        types = ['Select','Select','Date']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['Ninja','Tecnica','']
        return pointers
