from rest_framework.serializers import ModelSerializer
from api.models.Persona import Persona

class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        #fields = ['nombre','edad','sexo','clan','fecha_nacimiento']
        fields = "__all__"
