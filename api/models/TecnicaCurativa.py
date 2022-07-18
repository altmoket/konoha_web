from django.db import models
from api.models.Tecnica import Tecnica
class TecnicaCurativa(Tecnica):
    velocidad_curacion = models.IntegerField(default=0)
    def save(self, *args, **kargs):
        file = open("file.txt", "r")
        msg = file.read()
        file.close()
        print(msg)
        self.id = int(msg)
        objecto=Tecnica.objects.filter(id=self.id)
        if len(objecto)>0:
            self.nombre=objecto[0].nombre
            self.elemento=objecto[0].elemento
            self.es_oculta=objecto[0].es_oculta
            self.cantidad_chakra=objecto[0].cantidad_chakra
        print(objecto)
        super().save(*args, **kargs)
