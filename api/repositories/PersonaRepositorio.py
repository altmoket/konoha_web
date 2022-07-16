from api.models.Persona import Persona
class PersonaRepositorio:
    @staticmethod
    def listar():
        personas = Persona.objects.all().values()
        return personas
