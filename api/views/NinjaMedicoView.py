
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.NinjaMedico import NinjaMedico
from api.serializers.NinjaMedicoSerializer import NinjaMedicoSerializer
@api_view(['GET','POST'])
def ninja_medico_list(request):
    return get_post(request, NinjaMedico, NinjaMedicoSerializer)
@api_view(['GET','PUT','DELETE'])
def ninja_medico_detail(request,pk):
    return get_put_delete(request, pk, NinjaMedico, NinjaMedicoSerializer)

