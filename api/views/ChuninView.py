
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.Chunin import Chunin
from api.serializers.ChuninSerializer import ChuninSerializer

#chunins
@api_view(['GET','POST'])
def chunin_list(request):
    return get_post(request, Chunin, ChuninSerializer)
@api_view(['GET','PUT','DELETE'])
def chunin_detail(request,pk):
    return get_put_delete(request, pk, Chunin, ChuninSerializer)

