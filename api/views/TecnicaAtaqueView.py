
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.TecnicaAtaque import TecnicaAtaque
from api.serializers.TecnicaAtaqueSerializer import TecnicaAtaqueSerializer
#tecnicas ataque
@api_view(['GET','POST'])
def tecnica_ataque_list(request):
    return get_post(request, TecnicaAtaque, TecnicaAtaqueSerializer)
@api_view(['GET','PUT','DELETE'])
def tecnica_ataque_detail(request,pk):
    return get_put_delete(request, pk, TecnicaAtaque, TecnicaAtaqueSerializer)

