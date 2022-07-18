from django.db import models
from api.models.Persona import Persona
class Ninja(Persona):
    chakra_max = models.IntegerField(default=0)
    sobrenombre = models.CharField(max_length=50, default="")
    def save(self, *args, **kargs):
        try:
            file = open("file.txt", "r")
            msg = file.read()
            file.close()
            print(msg)
            self.id = int(msg)
        except Exception as e:
                print(e)
        objecto=Persona.objects.filter(id=self.id)
        if len(objecto)>0:
            self.nombre=objecto[0].nombre
            self.edad=objecto[0].edad
            self.clan=objecto[0].clan
            self.sexo=objecto[0].sexo
            self.fecha_nacimiento=objecto[0].fecha_nacimiento
        print(objecto)
        super().save(*args, **kargs)

