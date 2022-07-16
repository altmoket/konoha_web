from rest_framework.decorators import api_view

from django.db.models import Q

# Todos los modelos
from api.models.Persona import Persona
from api.models.Ninja import Ninja
from api.models.Genin import Genin
from api.models.Chunin import Chunin
from api.models.Tecnica import Tecnica
from api.models.TecnicaCurativa import TecnicaCurativa
from api.models.TecnicaAtaque import TecnicaAtaque
from api.models.NinjaMedico import NinjaMedico
from api.models.NinjaTecnica import NinjaTecnica
from api.models.Equipo import Equipo
from api.models.BestiaMitica import BestiaMitica
from api.models.BestiaMisionPergamino import BestiaMisionPergamino
from api.models.EquipoEnMision import EquipoEnMision
from api.models.EquipoEnMisionPergamino import EquipoEnMisionPergamino
from api.models.Jounin import Jounin
from api.models.Mision import Mision


#consultas
@api_view(['GET'])
def female_medical_ninjas(request):
    female_medical_ninjas=NinjaMedico.objects.filter(sexo='F')
    medical_ninjas=NinjaMedico.objects.all()
    percent=(len(female_medical_ninjas) * 100) / len(medical_ninjas)
    return Response(percent)

@api_view(['GET'])
def captain_in_C_rank_missions(request):
    team_on_mission=EquipoEnMision.objects.all()
    captain_missions=[(item.capitan,item.mision) for item in team_on_mission
                     if item.mision.rango== 'B' or item.mision.rango=='A' or item.mision.rango=='S']
    dicc=dict()
    for item in captain_missions:
        if dicc.has_key(item[0]):
            dicc[item[0]]=dicc[item[0]]+1
        else:
            dicc.setdefault(item[0],1)
    captain_list={captain for (captain,missions) in dicc.items() if missions>3}
    return Response(captain_list)

@api_view(['GET'])
def ninja_invocation_in_S_rank_missions(request):
    team_on_mission=EquipoEnMision.objects.all()
    ninjas_S_rank_missions=[(item.equipo,item.capitan) for item in team_on_mission if item.mision.rango==S]
    dicc=dict()
    for item in ninjas_S_rank_missions:
        if dicc.has_key(item[0].ninja1):
            dicc[item[0].ninja1]=dicc[item[0].ninja1]+1
        else:
            dicc.setdefault(item[0].ninja1,1)
        if dicc.has_key(item[0].ninja2):
            dicc[item[0].ninja2]=dicc[item[0].ninja2]+1
        else:
            dicc.setdefault(item[0].ninja2,1)
        if dicc.has_key(item[0].ninjamedico):
            dicc[item[0].ninjamedico]=dicc[item[0].ninjamedico]+1
        else:
            dicc.setdefault(item[0].ninjamedico,1)
        if dicc.has_key(item[1]):
            dicc[item[1]]=dicc[item[1]]+1
        else:
            dicc.setdefault(item[1],1)
    ninjas=[ninja for (ninja,missions) in dicc.items() if missions>6]
    ninjas_invocation=[(item.invocador.nombre,item.invocador.clan,item.nombre) for item in BestiaMitica if ninjas.__contains__(item.invocador)]
    return Response(ninjas_invocation)

@api_view(['GET'])
def hidden_techniques(request):
    foreign_missions=EquipoEnMision.objects.filter(mision_in=[mision.id for mision in Mision.objects.filter(~Q(pais_cliente="Konoa"))])
    ocult_technique=NinjaTecnica.objects.filter(tecnica_in=[tecnica.id for tecnica in Tecnica.objects.filter(es_oculta=True)])
    dicc=dict()
    for (ninja,tecnica) in ocult_technique:
        for item in foreign_missions:
            if item.capitan==ninja:
                if dicc.has_key(item.capitan):
                    dicc[item.capitan].add(tecnica)
                else:
                    dicc.setdefault(item.capitan,tecnica)
            elif item.equipo.ninja1==ninja:
                if dicc.has_key(item.equipo.ninja1):
                    dicc[item.equipo.ninja1].add(tecnica)
                else:
                    dicc.setdefault(item.equipo.ninja1,tecnica)
            elif item.equipo.ninja2==ninja:
                if dicc.has_key(item.equipo.ninja2):
                    dicc[item.equipo.ninja2].add(tecnica)
                else:
                    dicc.setdefault(item.equipo.ninja2,tecnica)
            elif item.equipo.ninjamedico==ninja:
                if dicc.has_key(item.equipo.ninjamedico):
                    dicc[item.equipo.ninjamedico].add(tecnica)
                else:
                    dicc.setdefault(item.equipo.ninjamedico,tecnica)
    hidden_techn=dicc.values()
    return Response(hidden_techn)

@api_view(['GET'])        
def medical_ninja_captains(request):
    medical_ninja=NinjaMedico.objects.all()
    team_on_mission=EquipoEnMision.objects.all()
    medical_captain=[item.capitan for item in team_on_mission if medical_ninja.__contains__(item.capitan)]
    return Response(medical_captain)

@api_view(['GET'])
def highest_reward_missions(request):
    satisfactory_mission=EquipoEnMision.objects.filter(resultado='S').order_by(mision.recompensa)
    missions=satisfactory_mission.values_list('mision',flat=True).order_by('recompensa')
    return Response(missions)
