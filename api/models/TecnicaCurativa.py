from django.db import models
from api.models.Tecnica import Tecnica
class TecnicaCurativa(Tecnica):
    velocidad_curacion = models.IntegerField(default=0)
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.elemento
        yield self.es_oculta
        yield self.cantidad_chakra
        yield self.velocidad_curacion
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
