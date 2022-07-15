from rest_framework.viewsets import ModelViewSet

from api.models.Ninja import Ninja
from api.models.Persona import Persona
from api.serializers.NinjaSerializer import NinjaSerializer
from api.serializers.PersonaSerializer import PersonaSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
class PersonaViewSet(ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    @action(detail=True, methods=['get'])
    def become_in_ninja(self, request, pk=None):
        persona = self.get_object()
        page = self.paginate_queryset(persona)
        if page is not None:
            serializer = self.get_serializer(page,many=False)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(persona, many=False)
        return Response(serializer.data)
