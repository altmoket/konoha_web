
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.EquipoEnMision import EquipoEnMision
from api.serializers.EquipoEnMisionSerializer import EquipoEnMisionSerializer
#equipos en misiones
@api_view(['GET','POST'])
def equipo_en_mision_list(request):
    return get_post(request, EquipoEnMision, EquipoEnMisionSerializer)
@api_view(['GET','PUT','DELETE'])
def equipo_en_mision_detail(request,pk):
    return get_put_delete(request, pk, EquipoEnMision, EquipoEnMisionSerializer)

