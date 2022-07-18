from django.db import models
from api.models.Ninja import Ninja
from api.models.NinjaMedico import NinjaMedico
class Equipo(models.Model):
    nombre = models.CharField(max_length=50, default="")
    ninja1 = models.OneToOneField(Ninja, on_delete=models.CASCADE, related_name='exceptuar_ninja_1', null=False, primary_key=True)
    ninja2 = models.ForeignKey(Ninja, on_delete=models.CASCADE, related_name='exceptuar_ninja_2', null=False)
    ninjamedico = models.ForeignKey(NinjaMedico, on_delete=models.CASCADE, null=False)
    def save_element(self, *args, **kargs):
        return super().save(*args, **kargs)
    def __str__(self):
        return str(self.nombre) + '('+ str(self.pk) + ')'
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.ninja1
        yield self.ninja2
        yield self.ninjamedico
    def add_values(self, values):
        headers = Equipo.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'ID Ninja1':
                self.ninja1 = values[i]
            elif headers[i] == 'ID Ninja2':
                self.ninja2 = values[i]
            elif headers[i] == 'ID Ninja Medico':
                self.ninjamedico = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID', 'Nombre', 'ID Ninja1', 'ID Ninja2', 'ID Ninja Medico']
        return headers
    class Meta:
        unique_together = [['ninja1','ninja2','ninjamedico']]
    @staticmethod
    def get_types():
        types = ['Char','Select','Select','Select']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['','Ninja','Ninja','NinjaMedico']
        return pointers
