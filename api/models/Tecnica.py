from django.db import models
class Tecnica(models.Model):
    nombre = models.CharField(max_length=50, default="")
    elemento = models.CharField(max_length=30, default="")
    es_oculta = models.BooleanField(default=False)
    cantidad_chakra = models.IntegerField(default=0)
    @staticmethod
    def get_headers():
        headers = ['ID', 'Nombre', 'Elemento', 'Es Oculta', 'Cantidad Chakra']
        return headers
