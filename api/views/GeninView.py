
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.Genin import Genin
from api.serializers.GeninSerializer import GeninSerializer

#genins
@api_view(['GET','POST'])
def genin_list(request):
    return get_post(request, Genin, GeninSerializer)
@api_view(['GET','PUT','DELETE'])
def genin_detail(request,pk):
    return get_put_delete(request, pk, Genin, GeninSerializer)

