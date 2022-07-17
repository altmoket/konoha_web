from django.db import models
from datetime import date
from api.models.Equipo import Equipo
from api.models.Mision import Mision
from api.models.Jounin import Jounin
class EquipoEnMision(models.Model):
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE, null=False, primary_key=True)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE, null=False)
    fecha_inicio = models.DateField(default=date(1,1,1))
    fecha_fin = models.DateField(default=date(1,1,1))
    RESULT = (
        ('S','Satisfactorio'),
        ('NS', 'No Satisfactorio'),
        ('P', 'Pendiente')
    )
    resultado = models.CharField(max_length=20,choices=RESULT, default='P')
    cantidad_shurikens = models.IntegerField(default=0)
    cantidad_kunais = models.IntegerField(default=0)
    cantidad_sellos = models.IntegerField(default=0)
    capitan = models.ForeignKey(Jounin, on_delete=models.CASCADE, null=False)
    def __iter__(self):
        yield self.pk
        yield self.equipo
        yield self.mision
        yield self.fecha_inicio
        yield self.fecha_fin
        yield self.resultado
        yield self.cantidad_shurikens
        yield self.cantidad_kunais
        yield self.cantidad_sellos
        yield self.capitan
    def add_values(self, values):
        headers = EquipoEnMision.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'ID Equipo':
                self.equi = values[i]
            elif headers[i] == 'ID Mision':
                self.misi = values[i]
            elif headers[i] == 'Fecha Inicio':
                self.fecha_inicio = values[i]
            elif headers[i] == 'Fecha Fin':
                self.fecha_fin = values[i]
            elif headers[i] == 'Resultado':
                self.resultado = values[i]
            elif headers[i] == 'Cantidad Shurikens':
                self.cantidad_shurikens = values[i]
            elif headers[i] == 'Cantidad Kunais':
                self.cantidad_kunais = values[i]
            elif headers[i] == 'Cantidad Sellos':
                self.cantidad_sellos = values[i]
            elif headers[i] == 'Capitan':
                self.capitan = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID','ID Equipo', 'ID Mision', 'Fecha Inicio', 'Fecha Fin', 'Resultado', 'Cantidad Shurikens', 'Cantidad Kunais','Cantidad Sellos', 'Capitan']
        return headers
    class Meta:
        unique_together = [['equipo','mision']]
    @staticmethod
    def get_types():
        types = ['Select','Select','Date','Date','Choices','Int','Int','Int','Select']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['Equipo','Mision','','',['S','SN','P'],'','','','Jounin']
        return pointers
