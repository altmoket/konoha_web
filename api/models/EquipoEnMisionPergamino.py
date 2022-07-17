from django.db import models
from api.models.EquipoEnMision import EquipoEnMision
from api.models.Pergamino import Pergamino
class EquipoEnMisionPergamino(models.Model):
    equipoenmision = models.OneToOneField(EquipoEnMision, on_delete=models.CASCADE, null=False, primary_key=True)
    pergamino = models.ForeignKey(Pergamino, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return 'BMP(' + str(self.pk) + ')'
    def __iter__(self):
        yield self.pk
        yield self.equipoenmision
        yield self.pergamino
    def add_values(self, values):
        headers = EquipoEnMisionPergamino.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'ID Equipo En Mision':
                self.equipoenmision = values[i]
            elif headers[i] == 'ID Pergamino':
                self.pergamino = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID','ID Equipo En Mision', 'ID Pergamino']
        return headers
    @staticmethod
    def get_types():
        types = ['Select','Select']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['EquipoEnMision','Pergamino']
        return pointers
    class Meta:
        unique_together = [['equipoenmision','pergamino']]
