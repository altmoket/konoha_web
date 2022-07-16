
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.Tecnica import Tecnica
from api.serializers.TecnicaSerializer import TecnicaSerializer
#tecnicas
@api_view(['GET','POST'])
def tecnica_list(request):
    return get_post(request, Tecnica, TecnicaSerializer)
@api_view(['GET','PUT','DELETE'])
def tecnica_detail(request,pk):
    return get_put_delete(request, pk, Tecnica, TecnicaSerializer)

