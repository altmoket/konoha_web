
from api.models.BestiaMisionPergamino import BestiaMisionPergamino
from api.models.BestiaMitica import BestiaMitica
from api.models.Chunin import Chunin
from api.models.Equipo import Equipo
from api.models.EquipoEnMision import EquipoEnMision
from api.models.EquipoEnMisionPergamino import EquipoEnMisionPergamino
from api.models.Genin import Genin
from api.models.Jounin import Jounin
from api.models.Mision import Mision
from api.models.Ninja import Ninja
from api.models.NinjaMedico import NinjaMedico
from api.models.NinjaTecnica import NinjaTecnica
from api.models.Pergamino import Pergamino
from api.models.Persona import Persona
from api.models.Tecnica import Tecnica
from api.models.TecnicaAtaque import TecnicaAtaque
from api.models.TecnicaCurativa import TecnicaCurativa


modelsName = ['Persona', 'Ninja', 'Genin', 'Chunin', 'Jounin', 'Tecnica', 'TecnicaAtaque', 'TecnicaCurativa', 'NinjaTecnica', 'NinjaMedico', 'Equipo', 'Mision', 'EquipoEnMision', 'Pergamino', 'EquipoEnMisionPergamino', 'BestiaMitica', 'BestiaMisionPergamino']
models = {'Persona':Persona, 'Ninja':Ninja, 'Genin':Genin, 'Chunin':Chunin, 'Jounin':Jounin, 'Tecnica':Tecnica, 'TecnicaAtaque':TecnicaAtaque, 'TecnicaCurativa':TecnicaCurativa, 'NinjaTecnica':NinjaTecnica, 'NinjaMedico':NinjaMedico, 'Equipo':Equipo, 'Mision':Mision, 'EquipoEnMision':EquipoEnMision, 'Pergamino':Pergamino, 'EquipoEnMisionPergamino':EquipoEnMisionPergamino, 'BestiaMitica':BestiaMitica, 'BestiaMisionPergamino':BestiaMisionPergamino}
headers = {'Persona':Persona.get_headers(), 'Ninja':Ninja.get_headers(), 'Genin':Genin.get_headers(), 'Chunin':Chunin.get_headers(), 'Jounin':Jounin.get_headers(), 'Tecnica':Tecnica.get_headers(), 'TecnicaAtaque':TecnicaAtaque.get_headers(), 'TecnicaCurativa':TecnicaCurativa.get_headers(), 'NinjaTecnica':NinjaTecnica.get_headers(), 'NinjaMedico':NinjaMedico.get_headers(), 'Equipo':Equipo.get_headers(), 'Mision':Mision.get_headers(), 'EquipoEnMision':EquipoEnMision.get_headers(), 'Pergamino':Pergamino.get_headers(), 'EquipoEnMisionPergamino':EquipoEnMisionPergamino.get_headers(), 'BestiaMitica':BestiaMitica.get_headers(), 'BestiaMisionPergamino':BestiaMisionPergamino.get_headers()}

def exist_model(data):
    for model in modelsName:
        if data == model:
            return True
    return False
def get_model(data):
    return models[data]

def get_headers(data):
    return headers[data]

def get_types(data):
    model = models[data]
    return model.get_types() 

def get_pointers(data):
    model = models[data]
    return model.get_pointers() 
    
    
