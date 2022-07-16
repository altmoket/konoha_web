from rest_framework.decorators import api_view
from api.helpers import get_post, get_put_delete
from api.models.Persona import Persona
from api.serializers.PersonaSerializer import PersonaSerializer

#personas
@api_view(['GET','POST'])
def persona_list(request):
    return get_post(request, Persona, PersonaSerializer)
@api_view(['GET','PUT','DELETE'])
def persona_detail(request,pk):
    return get_put_delete(request, pk, Persona, PersonaSerializer)

