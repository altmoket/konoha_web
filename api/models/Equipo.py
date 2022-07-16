from django.db import models
from api.models.Ninja import Ninja
from api.models.NinjaMedico import NinjaMedico
class Equipo(models.Model):
    nombre = models.CharField(max_length=50, default="")
    ninja1 = models.OneToOneField(Ninja, on_delete=models.CASCADE, related_name='exceptuar_ninja_1', null=False, primary_key=True)
    ninja2 = models.ForeignKey(Ninja, on_delete=models.CASCADE, related_name='exceptuar_ninja_2', null=False)
    ninjamedico = models.ForeignKey(NinjaMedico, on_delete=models.CASCADE, null=False)
    @staticmethod
    def get_headers():
        headers = ['ID', 'Nombre', 'ID Ninja1', 'ID Ninja2', 'ID Ninja Medico']
        return headers
    class Meta:
        unique_together = [['ninja1','ninja2','ninjamedico']]
