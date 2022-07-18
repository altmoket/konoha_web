from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Chunin(Ninja):
    fecha_examen = models.DateField(default=date(1,1,1))
    calificacion_examen = models.CharField(max_length=100, default="")
    def save(self, *args, **kargs):
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
        print(objecto)
        super().save(*args, **kargs)
