from django.db import models
from api.models.Ninja import Ninja
from api.models.Tecnica import Tecnica
class NinjaTecnica(models.Model):
    ninja = models.OneToOneField(Ninja, on_delete=models.CASCADE, null=False, primary_key=True)
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, null=False)
    def __iter__(self):
        yield self.pk
        yield self.ninja
        yield self.tecnica
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
