from rest_framework.serializers import ModelSerializer
from api.models.Ninja import Ninja

class NinjaSerializer(ModelSerializer):
    class Meta:
        model = Ninja
        fields = "__all__"
