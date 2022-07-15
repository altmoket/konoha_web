from django.db import models
import uuid
from datetime import date
class Persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
