
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.BestiaMisionPergamino import BestiaMisionPergamino
from api.serializers.BestiaMisionPergaminoSerializer import BestiaMisionPergaminoSerializer

#bestias misiones pergamino
@api_view(['GET','POST'])
def bestia_mision_pergamino_list(request):
    return get_post(request, BestiaMisionPergamino, BestiaMisionPergaminoSerializer)
@api_view(['GET','PUT','DELETE'])
def bestia_mision_pergamino_detail(request,pk):
    return get_put_delete(request, pk, BestiaMisionPergamino, BestiaMisionPergaminoSerializer)

