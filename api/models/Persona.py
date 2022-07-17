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

    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento
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
