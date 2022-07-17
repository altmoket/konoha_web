
from api.models.Ninja import Ninja
class NinjaMedico(Ninja):
    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento
        yield self.chakra_max
        yield self.sobrenombre
    @staticmethod
    def get_headers():
        headers = Ninja.get_headers()
        return headers
    @staticmethod
    def get_types():
        types = Ninja.get_types()
        return types
    @staticmethod
    def get_pointers():
        pointers = Ninja.get_pointers()
        return pointers
