from rest_framework.decorators import api_view

from django.db.models import Q

from rest_framework.response import Response

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

# Todos los serializadores
from api.serializers.PersonaSerializer import PersonaSerializer
from api.serializers.NinjaSerializer import NinjaSerializer
from api.serializers.GeninSerializer import GeninSerializer
from api.serializers.ChuninSerializer import ChuninSerializer
from api.serializers.TecnicaSerializer import TecnicaSerializer
from api.serializers.TecnicaCurativaSerializer import TecnicaCurativaSerializer
from api.serializers.TecnicaAtaqueSerializer import TecnicaAtaqueSerializer
from api.serializers.NinjaMedicoSerializer import NinjaMedicoSerializer
from api.serializers.NinjaTecnicaSerializer import NinjaTecnicaSerializer
from api.serializers.EquipoSerializer import EquipoSerializer
from api.serializers.BestiaMiticaSerializer import BestiaMiticaSerializer
from api.serializers.BestiaMisionPergaminoSerializer import BestiaMisionPergaminoSerializer
from api.serializers.EquipoEnMisionSerializer import EquipoEnMisionSerializer
from api.serializers.EquipoEnMisionPergaminoSerializer import EquipoEnMisionPergaminoSerializer
from api.serializers.JouninSerializer import JouninSerializer
from api.serializers.MisionSerializer import MisionSerializer
from api.serializers.PergaminoSerializer import PergaminoSerializer


#consultas
@api_view(['GET'])
def female_medical_ninjas(request):
    try:
        female_medical_ninjas=NinjaMedico.objects.filter(sexo='F')
        medical_ninjas=NinjaMedico.objects.all()
        percent=(len(female_medical_ninjas) * 100) / len(medical_ninjas)
    except Exception as e:
        raise e
    return Response(percent)

@api_view(['GET'])
def captain_in_C_rank_missions(request):
    try:
        team_on_mission=EquipoEnMision.objects.all()
        captain_missions=[(item.capitan,item.mision) for item in team_on_mission
                        if item.mision.rango== 'B' or item.mision.rango=='A' or item.mision.rango=='S']
        dicc=dict()
        for item in captain_missions:
            if dicc.__contains__(item[0]):
                dicc[item[0]]=dicc[item[0]]+1
            else:
                dicc.setdefault(item[0],1)
        captain_list=[captain for (captain,missions) in dicc.items() if missions>3]
        serializer=JouninSerializer(captain_list,many=True)
        return Response(serializer.data)
    except Exception as e:
        raise e

@api_view(['GET'])
def ninja_invocation_in_S_rank_missions(request):
    team_on_mission=EquipoEnMision.objects.all()
    ninjas_S_rank_missions=[(item.equipo,item.capitan) for item in team_on_mission if item.mision.rango=='S']
    print(ninjas_S_rank_missions)
    dicc=dict()
    for item in ninjas_S_rank_missions:
        if dicc.__contains__(item[0].ninja1):
            dicc[item[0].ninja1]=dicc[item[0].ninja1]+1
        else:
            dicc.setdefault(item[0].ninja1,1)
        if dicc.__contains__(item[0].ninja2):
            dicc[item[0].ninja2]=dicc[item[0].ninja2]+1
        else:
            dicc.setdefault(item[0].ninja2,1)
        if dicc.__contains__(item[0].ninjamedico):
            dicc[item[0].ninjamedico]=dicc[item[0].ninjamedico]+1
        else:
            dicc.setdefault(item[0].ninjamedico,1)
        if dicc.__contains__(item[1]):
            dicc[item[1]]=dicc[item[1]]+1
        else:
            dicc.setdefault(item[1],1)
    ninjas={ninja.id:ninja for (ninja,missions) in dicc.items() if missions>6}
    print(ninjas)
    ninjas_invocation=[(item.invocador.nombre,item.invocador.clan,item.nombre) for item in BestiaMitica.objects.all() if ninjas.__contains__(item.invocador.id)]
    # ninjas_invocation=[]
    # for item in ninjas:
    #     for bestia in BestiaMitica.objects.all():
    #         print(item)
    #         print(bestia.invocador.nombre)
    #         if(item.id==bestia.invocador.id):
    #             print("estoy aqui")
    #             ninjas_invocation.append((item.nombre,item.clan,bestia.nombre))
    print(ninjas_invocation)
    return Response(ninjas_invocation)


@api_view(['GET'])
def hidden_techniques(request):
    foreign_missions=EquipoEnMision.objects.filter(mision__in=[mision.id for mision in Mision.objects.filter(~Q(pais_cliente="Konoha"))])
    ocult_technique=NinjaTecnica.objects.filter(tecnica__in=[tecnica.id for tecnica in Tecnica.objects.filter(es_oculta=True)])
    dicc=dict()
    for ninja_tecnica in ocult_technique:
        for item in foreign_missions:
            if item.capitan==ninja_tecnica.ninja:
                if dicc.__contains__(item.capitan):
                    dicc[item.capitan].append(ninja_tecnica.tecnica)
                else:
                    dicc.setdefault(item.capitan,[ninja_tecnica.tecnica])
            elif item.equipo.ninja1==ninja_tecnica.ninja:
                if dicc.__contains__(item.equipo.ninja1):
                    dicc[item.equipo.ninja1].append(ninja_tecnica.tecnica)
                else:
                    dicc.setdefault(item.equipo.ninja1,[ninja_tecnica.tecnica])
            elif item.equipo.ninja2==ninja_tecnica.ninja:
                if dicc.__contains__(item.equipo.ninja2):
                    dicc[item.equipo.ninja2].append(ninja_tecnica.tecnica)
                else:
                    dicc.setdefault(item.equipo.ninja2,[ninja_tecnica.tecnica])
            elif item.equipo.ninjamedico==ninja_tecnica.ninja:
                if dicc.__contains__(item.equipo.ninjamedico):
                    dicc[item.equipo.ninjamedico].append(ninja_tecnica.tecnica)
                else:
                    dicc.setdefault(item.equipo.ninjamedico,[ninja_tecnica.tecnica])
    hidden_techn=dicc.values()
    lista=[]
    for item in hidden_techn:
        lista+item
        for var in item:
            if not lista.__contains__(var):
                lista.append(var)
    serializer=TecnicaSerializer(lista,many=True)
    return Response(serializer.data)

@api_view(['GET'])        
def medical_ninja_captains(request):
    medical_ninja=NinjaMedico.objects.all()
    medical_ninja_dicc={item.id:item for item in medical_ninja}
    print(medical_ninja)
    team_on_mission=EquipoEnMision.objects.all()
    print(team_on_mission)
    medical_captain=[item.capitan for item in team_on_mission if medical_ninja_dicc.__contains__(item.capitan.id)]
    medical_captain_list=[]
    for item in medical_captain:
        if not medical_captain_list.__contains__(item):
            medical_captain_list.append(item)
    serializer=JouninSerializer(medical_captain_list,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def highest_reward_missions(request):
    satisfactory_mission=EquipoEnMision.objects.filter(resultado='S')
    missions=satisfactory_mission.values_list('mision',flat=True).order_by('recompensa')
    return Response(missions)