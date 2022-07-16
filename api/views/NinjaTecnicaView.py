
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.NinjaTecnica import NinjaTecnica
from api.serializers.NinjaTecnicaSerializer import NinjaTecnicaSerializer
#ninja tecnicas
@api_view(['GET','POST'])
def ninja_tecnica_list(request):
    return get_post(request, NinjaTecnica, NinjaTecnicaSerializer)
@api_view(['GET','PUT','DELETE'])
def ninja_tecnica_detail(request,pk):
    return get_put_delete(request, pk, NinjaTecnica, NinjaTecnicaSerializer)

