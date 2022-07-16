

from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.Ninja import Ninja
from api.serializers.NinjaSerializer import NinjaSerializer

#ninjas
@api_view(['GET','POST'])
def ninja_list(request):
    return get_post(request, Ninja, NinjaSerializer)
@api_view(['GET','PUT','DELETE'])
def ninja_detail(request,pk):
    return get_put_delete(request, pk, Ninja, NinjaSerializer)

