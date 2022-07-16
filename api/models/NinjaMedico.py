
from api.models.Ninja import Ninja
class NinjaMedico(Ninja):
    @staticmethod
    def get_headers():
        headers = Ninja.get_headers()
        return headers
    pass
