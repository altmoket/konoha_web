from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Genin(Ninja):
    fecha_graduacion = models.DateField(default=date(1,1,1))
    valoracion = models.CharField(max_length=200, default="")
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
        

