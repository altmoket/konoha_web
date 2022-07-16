
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.Equipo import Equipo
from api.serializers.EquipoSerializer import EquipoSerializer
#equipos
@api_view(['GET','POST'])
def equipo_list(request):
    return get_post(request, Equipo, EquipoSerializer)
@api_view(['GET','PUT','DELETE'])
def equipo_detail(request,pk):
    return get_put_delete(request, pk, Equipo, EquipoSerializer)

