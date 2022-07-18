from django.db import models
from datetime import date
class Persona(models.Model):
    nombre = models.CharField(max_length=50, default="")
    edad = models.IntegerField(default=12)
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No se dice')
    )
    sexo = models.CharField(max_length=1,choices=SEX, default='N')
    clan = models.CharField(max_length=50, default='Konoha')
    fecha_nacimiento = models.DateField(default=date(1,1,1))

    def __str__(self):
        return str(self.nombre) + '('+ str(self.pk) + ')'
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento

    def add_values(self, values):
        headers = Persona.get_headers()
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
    @staticmethod
    def get_headers():
        headers = ['ID', 'Nombre', 'Edad', 'Sexo', 'Clan', 'Fecha Nacimiento']
        return headers
    @staticmethod
    def get_types():
        types = ['Char','Int','Choices','Char','Date']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['','',['M','F','N'],'','']
        return pointers
