from django.db import models
from api.models.Ninja import Ninja
from api.models.Tecnica import Tecnica
class NinjaTecnica(models.Model):
    ninja = models.OneToOneField(Ninja, on_delete=models.CASCADE, null=False, primary_key=True)
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return 'NT(' + str(self.pk) + ')'
    def __iter__(self):
        yield self.pk
        yield self.ninja
        yield self.tecnica
    def add_values(self, values):
        headers = NinjaTecnica.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'ID Ninja':
                self.ninja = values[i]
            elif headers[i] == 'ID Tecnica':
                self.tecnica = values[i]
    @staticmethod
    def get_headers():
        headers = ['ID', 'ID Ninja', 'ID Tecnica']
        return headers
    @staticmethod
    def get_types():
        types = ['Select','Select']
        return types
    @staticmethod
    def get_pointers():
        pointers = ['Ninja','Tecnica']
        return pointers
    class Meta:
        unique_together = [['ninja','tecnica']]
