
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverview(_):
    api_urls = {
        'Listar Cualquier cosa':'/listar/<str:data>',
        'Obtener Eliminar Actualizar':'/<str:data>/<int:pk>',
        'Crear':'/crear/',

        'Female-Medical-Ninjas': '/female-medical-ninjas/',

        'Captain-In-C-Rank-Missions': '/captain-in-C-rank-missions/',

        'Ninja-Invocation-In-S-Rank-Missions': '/ninja-invocation-in-S-rank-missions/',

        'Hidden-Techniques': '/hidden-techniques/',

        'Medical-Ninja-Captains': '/medical-ninja-captains/',
        
        'Highest-Reward-Missions': '/highest-reward-missions/',
    }
    return Response(api_urls)
