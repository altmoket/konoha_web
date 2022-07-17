from django.db import models
class Mision(models.Model):
    cliente = models.CharField(max_length=50, default="")
    pais_cliente = models.CharField(max_length=30, default="")
    rango = models.CharField(max_length=1, default='')
    recompensa = models.IntegerField(default=0)
    def __iter__(self):
        yield self.pk
        yield self.cliente
        yield self.pais_cliente
        yield self.rango
        yield self.recompensa
    def add_values(self, values):
        headers = Mision.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Cliente':
                self.cliente = values[i]
            elif headers[i] == 'Pais Cliente':
                self.pais_cliente = values[i]
            elif headers[i] == 'Rango':
                self.rango = values[i]
            elif headers[i] == 'Recompensa':
                self.recompensa = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID', 'Cliente', 'Pais Cliente', 'Rango', 'Recompensa']
        return headers
    @staticmethod
    def get_types():
        types = ['Char','Char','Char','Int']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['','','','']
        return pointers
