
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.TecnicaCurativa import TecnicaCurativa
from api.serializers.TecnicaCurativaSerializer import TecnicaCurativaSerializer
#tecnicas curativas
@api_view(['GET','POST'])
def tecnica_curativa_list(request):
    return get_post(request, TecnicaCurativa, TecnicaCurativaSerializer)
@api_view(['GET','PUT','DELETE'])
def tecnica_curativa_detail(request,pk):
    return get_put_delete(request, pk, TecnicaCurativa, TecnicaCurativaSerializer)

