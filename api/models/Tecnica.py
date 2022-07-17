from django.db import models
class Tecnica(models.Model):
    nombre = models.CharField(max_length=50, default="")
    elemento = models.CharField(max_length=30, default="")
    es_oculta = models.BooleanField(default=False)
    cantidad_chakra = models.IntegerField(default=0)
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.elemento
        yield self.es_oculta
        yield self.cantidad_chakra
    def add_values(self, values):
        headers = Tecnica.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'Elemento':
                self.elemento = values[i]
            elif headers[i] == 'Es Oculta':
                self.es_oculta = values[i]
            elif headers[i] == 'Cantidad Chakra':
                self.cantidad_chakra = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID', 'Nombre', 'Elemento', 'Es Oculta', 'Cantidad Chakra']
        return headers
    @staticmethod
    def get_types():
        types = ['Char','Char','Boolean','Int']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['','','','']
        return pointers
