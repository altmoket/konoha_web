from rest_framework.viewsets import ModelViewSet

from api.models.Ninja import Ninja
from api.serializers.NinjaSerializer import NinjaSerializer
class NinjaViewSet(ModelViewSet):
    queryset = Ninja.objects.all()
    serializer_class = NinjaSerializer
