
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.Pergamino import Pergamino
from api.serializers.PergaminoSerializer import PergaminoSerializer
#pergaminos
@api_view(['GET','POST'])
def pergamino_list(request):
    return get_post(request, Pergamino, PergaminoSerializer)
@api_view(['GET','PUT','DELETE'])
def pergamino_detail(request,pk):
    return get_put_delete(request, pk, Pergamino, PergaminoSerializer)

