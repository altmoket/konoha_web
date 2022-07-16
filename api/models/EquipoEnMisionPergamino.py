from django.db import models
from api.models.EquipoEnMision import EquipoEnMision
from api.models.Pergamino import Pergamino
class EquipoEnMisionPergamino(models.Model):
    equipoenmision = models.OneToOneField(EquipoEnMision, on_delete=models.CASCADE, null=False, primary_key=True)
    pergamino = models.ForeignKey(Pergamino, on_delete=models.CASCADE, null=False)
    def __iter__(self):
        yield self.pk
        yield self.equipoenmision
        yield self.pergamino
    @staticmethod
    def get_headers():
        headers = ['ID','ID Equipo En Mision', 'ID Pergamino']
        return headers
    class Meta:
        unique_together = [['equipoenmision','pergamino']]
