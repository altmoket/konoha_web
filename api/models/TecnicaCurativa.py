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
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.elemento
        yield self.es_oculta
        yield self.cantidad_chakra
        yield self.velocidad_curacion
    def add_values(self, values):
        headers = TecnicaCurativa.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'Elemento':
                self.edad = values[i]
            elif headers[i] == 'Es Oculta':
                self.sexo = values[i]
            elif headers[i] == 'Cantidad Chakra':
                self.clan = values[i]
            elif headers[i] == 'Velocidad Curacion':
                self.velocidad_curacion = values[i]
    @staticmethod
    def get_headers():
        headers = Tecnica.get_headers()
        headers.append('Velocidad Curacion')
        return headers
    @staticmethod
    def get_types():
        types = Tecnica.get_types()
        types.append('Int')
        return types
    @staticmethod
    def get_pointers():
        pointers = Tecnica.get_pointers()
        pointers.append('')
        return pointers
