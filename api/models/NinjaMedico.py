
from api.models.Ninja import Ninja
class NinjaMedico(Ninja):
    def save_element(self, *args, **kargs):
        return super().save_element(*args, **kargs)

    def save(self, *args, **kargs):
        file = open("file.txt", "r")
        msg = file.read()
        file.close()
        print(msg)
        self.id = int(msg)
        objecto=Ninja.objects.filter(id=self.id)
        if len(objecto)>0:
            self.nombre=objecto[0].nombre
            self.edad=objecto[0].edad
            self.clan=objecto[0].clan
            self.sexo=objecto[0].sexo
            self.fecha_nacimiento=objecto[0].fecha_nacimiento
            self.chakra_max=objecto[0].chakra_max
            self.sobrenombre=objecto[0].sobrenombre
        print(objecto)
        super().save(*args, **kargs)

    def __iter__(self):
        yield self.pk
        yield self.nombre
        yield self.edad
        yield self.sexo
        yield self.clan
        yield self.fecha_nacimiento
        yield self.chakra_max
        yield self.sobrenombre
    def add_values(self, values):
        headers = NinjaMedico.get_headers()
        headers.pop(0)
        for i in range(len(headers)):
            if headers[i] == 'Nombre':
                self.nombre = values[i]
            elif headers[i] == 'Edad':
                self.edad = values[i]
            elif headers[i] == 'Sexo':
                self.sexo = values[i]
            elif headers[i] == 'Clan':
                self.clan = values[i]
            elif headers[i] == 'Fecha Nacimiento':
                self.fecha_nacimiento = values[i]
            elif headers[i] == 'Chakra Maximo':
                self.chakra_max = values[i]
            elif headers[i] == 'Sobrenombre':
                self.sobrenombre = values[i]
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
