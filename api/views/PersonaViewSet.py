from rest_framework.viewsets import ModelViewSet
from api.models.Persona import Persona
from api.serializers.PersonaSerializer import PersonaSerializer
class PersonaViewSet(ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


