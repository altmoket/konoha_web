
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverview(_):
    api_urls = {
        'Persona-List': '/personas/',
        'Persona-Detail': '/personas/<str:pk>',

        'Ninja-List': '/ninjas/',
        'Ninja-Detail': '/ninjas/<str:pk>',
        
        'Genin-List': '/genins/',
        'Genin-Detail': '/genins/<str:pk>',
        
        'Chunin-List': '/chunins/',
        'Chunin-Detail': '/chunins/<str:pk>',
        
        'Jounin-List': '/jounins/',
        'Jounin-Detail': '/jounins/<str:pk>',
        
        'Tecnica-List': '/tecnicas/',
        'Tecnica-Detail': '/tecnicas/<str:pk>',
        
        'Tecnica-Ataque-List': '/tecnicas-ataque/',
        'Tecnica-Ataque-Detail': '/tecnicas-ataque/<str:pk>',
        
        'Tecnica-Curativa-List': '/tecnicas-curativas/',
        'Tecnica-Curativa-Detail': '/tecnicas-curativas/<str:pk>',
        
        'Ninja-Tecnica-List': '/ninjas-tecnicas/',
        'Ninja-Tecnica-Detail': '/ninjas-tecnicas/<str:pk>',
        'Bestia-Mitica-List': '/bestias-miticas/', 'Bestia-Mitica-Detail': '/bestias-miticas/<str:pk>',
        
        'Equipo-List': '/equipos/',
        'Equipo-Detail': '/equipos/<str:pk>',
        
        'Mision-List': '/misiones/',
        'Mision-Detail': '/misiones/<str:pk>',
        
        'Equipo-En-Mision-List': '/equipos-en-misiones/',
        'Equipo-En-Mision-Detail': '/equipos-en-misiones/<str:pk>',
        
        'Pergamino-List': '/pergaminos/',
        'Pergamino-Detail': '/pergaminos/<str:pk>',
        
        'Equipo-En-Mision-Pergamino-List': '/equipos-en-misiones-pergaminos/',
        'Equipo-En-Mision-Pergamino-Detail': '/equipos-en-misiones-pergaminos/<str:pk>',
        
        'Bestia-Mision-Pergamino-List': '/bestias-misiones-pergaminos/',
        'Bestia-Mision-Pergamino-Detail': '/bestias-misiones-pergaminos/<str:pk>',
    }
    return Response(api_urls)
