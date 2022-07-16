
from api.repositories.PersonaRepositorio import PersonaRepositorio

class PersonaControlador:
    @staticmethod
    def listar():
        return PersonaRepositorio.listar()        

