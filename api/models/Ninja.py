from django.db import models
from api.models.Persona import Persona
class Ninja(Persona):
    chakra_max = models.IntegerField(default=0)
    sobrenombre = models.CharField(max_length=50, default="")
    # def save(self, *args, **kargs):
    #     print("esto son los argumentos")
    #     print(args)
    #     ninja=Persona.objects.filter(id=1)
    #     print(ninja)
    #     super(Ninja,self).save()
    #     if len(ninja) == 0:
    #         new=Persona(id=self.id,nombre=self.nombre,edad=self.edad,sexo=self.sexo,clan=self.clan,fecha_nacimiento=self.fecha_nacimiento)
    #         new.save()
