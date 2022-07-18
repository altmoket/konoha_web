
from api.serializers.BestiaMisionPergaminoSerializer import BestiaMisionPergaminoSerializer
from api.serializers.BestiaMiticaSerializer import BestiaMiticaSerializer
from api.serializers.ChuninSerializer import ChuninSerializer
from api.serializers.EquipoEnMisionPergaminoSerializer import EquipoEnMisionPergaminoSerializer
from api.serializers.EquipoEnMisionSerializer import EquipoEnMisionSerializer
from api.serializers.EquipoSerializer import EquipoSerializer
from api.serializers.GeninSerializer import GeninSerializer
from api.serializers.JouninSerializer import JouninSerializer
from api.serializers.MisionSerializer import MisionSerializer
from api.serializers.NinjaMedicoSerializer import NinjaMedicoSerializer
from api.serializers.NinjaSerializer import NinjaSerializer
from api.serializers.NinjaTecnicaSerializer import NinjaTecnicaSerializer
from api.serializers.PergaminoSerializer import PergaminoSerializer
from api.serializers.PersonaSerializer import PersonaSerializer
from api.serializers.TecnicaAtaqueSerializer import TecnicaAtaqueSerializer
from api.serializers.TecnicaCurativaSerializer import TecnicaCurativaSerializer
from api.serializers.TecnicaSerializer import TecnicaSerializer


serializadores = {'Persona':PersonaSerializer, 'Ninja':NinjaSerializer, 'Genin':GeninSerializer, 'Chunin':ChuninSerializer, 'Jounin':JouninSerializer, 'Tecnica':TecnicaSerializer, 'TecnicaAtaque':TecnicaAtaqueSerializer, 'TecnicaCurativa':TecnicaCurativaSerializer, 'NinjaTecnica':NinjaTecnicaSerializer, 'NinjaMedico':NinjaMedicoSerializer, 'Equipo':EquipoSerializer, 'Mision':MisionSerializer, 'EquipoEnMision':EquipoEnMisionSerializer, 'Pergamino':PergaminoSerializer, 'EquipoEnMisionPergamino':EquipoEnMisionPergaminoSerializer, 'BestiaMitica':BestiaMiticaSerializer, 'BestiaMisionPergamino':BestiaMisionPergaminoSerializer}

def get_serializer(data):
    return serializadores[data]
    
