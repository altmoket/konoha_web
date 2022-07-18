from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Chunin(Ninja):
    fecha_examen = models.DateField(default=date(1,1,1))
    calificacion_examen = models.CharField(max_length=100, default="")
    def save(self, *args, **kargs):
        try:
            file = open("file.txt", "r")
            msg = file.read()
            file.close()
            print(msg)
            self.id = int(msg)
            objecto=Ninja.objects.filter(id=self.id)
            if len(objecto)>0:
                self.nombre=objecto[0].nombre
                self.edad=objecto[0].edad
                self.clan=objecto[0].clan
                self.sexo=objecto[0].sexo
                self.fecha_nacimiento=objecto[0].fecha_nacimiento
                self.chakra_max=objecto[0].chakra_max
                self.sobrenombre=objecto[0].sobrenombre
            super().save(*args, **kargs)
        except Exception as e:
            print(e)
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento
        yield self.chakra_max
        yield self.sobrenombre
        yield self.fecha_examen
        yield self.calificacion_examen
    def add_values(self, values):
        headers = Chunin.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'Edad':
                self.edad = values[i]
            elif headers[i] == 'Sexo':
                self.sexo = values[i]
            elif headers[i] == 'Clan':
                self.clan = values[i]
            elif headers[i] == 'Fecha Nacimiento':
                self.fecha_nacimiento = values[i]
            elif headers[i] == 'Chakra Maximo':
                self.chakra_max = values[i]
            elif headers[i] == 'Sobrenombre':
                self.sobrenombre = values[i]
            elif headers[i] == 'Fecha Examen':
                self.fecha_examen = values[i]
            elif headers[i] == 'Calificacion Examen':
                self.calificacion_examen = values[i]
    @staticmethod
    def get_headers():
        headers = Ninja.get_headers()
        headers.append('Fecha Examen')
        headers.append('Calificacion Examen')
        return headers
    @staticmethod
    def get_types():
        types = Ninja.get_types()
        types.append('Date')
        types.append('Int')
        return types
    @staticmethod
    def get_pointers():
        pointers = Ninja.get_pointers()
        pointers.append('')
        pointers.append('')
        return pointers
