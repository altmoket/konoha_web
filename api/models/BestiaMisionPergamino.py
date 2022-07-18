from django.db import models

from api.models.BestiaMitica import BestiaMitica
from api.models.Mision import Mision
from api.models.Pergamino import Pergamino
class BestiaMisionPergamino(models.Model):
    bestia = models.OneToOneField(BestiaMitica, on_delete=models.CASCADE, null=False, primary_key=True)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE, null=False)
    pergamino = models.ForeignKey(Pergamino, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return 'BMP(' + str(self.pk) + ')'
    def __iter__(self):
        yield self.pk
        yield self.bestia
        yield self.mision
        yield self.pergamino

    def add_values(self, values):
        headers = BestiaMisionPergamino.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'ID Bestia':
                self.bestia = values[i]
            elif headers[i] == 'ID Mision':
                self.mision = values[i]
            elif headers[i] == 'ID Pergamino':
                self.pergamino = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID', 'ID Bestia', 'ID Mision', 'ID Pergamino']
        return headers
    @staticmethod
    def get_types():
        types = ['Select','Select','Select']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['BestiaMitica','Mision','Pergamino']
        return pointers
    class Meta:
        unique_together =[ ['bestia','mision','pergamino']]
