
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.EquipoEnMisionPergamino import EquipoEnMisionPergamino
from api.serializers.EquipoEnMisionPergaminoSerializer import EquipoEnMisionPergaminoSerializer
#Equipos en mision pergaminos
@api_view(['GET','POST'])
def equipo_en_mision_pergamino_list(request):
    return get_post(request, EquipoEnMisionPergamino, EquipoEnMisionPergaminoSerializer)
@api_view(['GET','PUT','DELETE'])
def equipo_en_mision_pergamino_detail(request,pk):
    return get_put_delete(request, pk, EquipoEnMisionPergamino, EquipoEnMisionPergaminoSerializer)

