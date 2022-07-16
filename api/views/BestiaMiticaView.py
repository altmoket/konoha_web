
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.BestiaMitica import BestiaMitica
from api.serializers.BestiaMiticaSerializer import BestiaMiticaSerializer
#bestias miticas
@api_view(['GET','POST'])
def bestia_mitica_list(request):
    return get_post(request, BestiaMitica, BestiaMiticaSerializer)
@api_view(['GET','PUT','DELETE'])
def bestia_mitica_detail(request,pk):
    return get_put_delete(request, pk, BestiaMitica, BestiaMiticaSerializer)

