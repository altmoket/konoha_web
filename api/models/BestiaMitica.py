from django.db import models
from api.models.Ninja import Ninja
class BestiaMitica(models.Model):
    nombre = models.CharField(max_length=50, default="")
    tipo = models.CharField(max_length=30, default="")
    invocador = models.ForeignKey(Ninja, on_delete=models.SET_NULL,null=True)
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.tipo
        yield self.invocador
    def add_values(self, values):
        headers = BestiaMitica.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'Tipo':
                self.tipo = values[i]
            elif headers[i] == 'Invocador':
                self.invocador = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID', 'Nombre', 'Tipo', 'Invocador']
        return headers
    @staticmethod
    def get_types():
        types = ['Char','Char','Select']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['','','Ninja']
        return pointers
