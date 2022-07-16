
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.Mision import Mision
from api.serializers.MisionSerializer import MisionSerializer
#misiones
@api_view(['GET','POST'])
def mision_list(request):
    return get_post(request, Mision, MisionSerializer)
@api_view(['GET','PUT','DELETE'])
def mision_detail(request,pk):
    return get_put_delete(request, pk, Mision, MisionSerializer)

