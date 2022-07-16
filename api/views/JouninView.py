
from api.helpers import get_post, get_put_delete
from rest_framework.decorators import api_view

from api.models.Jounin import Jounin
from api.serializers.JouninSerializer import JouninSerializer
#jounins
@api_view(['GET','POST'])
def jounin_list(request):
    return get_post(request, Jounin, JouninSerializer)
@api_view(['GET','PUT','DELETE'])
def jounin_detail(request,pk):
    return get_put_delete(request, pk, Jounin, JouninSerializer)

