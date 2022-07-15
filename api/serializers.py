from rest_framework import serializers

# Todos los modelos
from api.models.Persona import Persona
from api.models.Ninja import Ninja
from api.models.Genin import Genin
from api.models.Chunin import Chunin
from api.models.Tecnica import Tecnica
from api.models.TecnicaCurativa import TecnicaCurativa
from api.models.TecnicaAtaque import TecnicaAtaque
from api.models.NinjaMedico import NinjaMedico
from api.models.NinjaTecnica import NinjaTecnica
from api.models.Equipo import Equipo
from api.models.BestiaMitica import BestiaMitica
from api.models.BestiaMisionPergamino import BestiaMisionPergamino
from api.models.EquipoEnMision import EquipoEnMision
from api.models.EquipoEnMisionPergamino import EquipoEnMisionPergamino
from api.models.Jounin import Jounin
from api.models.Mision import Mision
from api.models.Pergamino import Pergamino

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
class NinjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ninja
        fields = '__all__'
class GeninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genin
        fields = '__all__'
class ChuninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chunin
        fields = '__all__'
class JouninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jounin
        fields = '__all__'
class TecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnica
        fields = '__all__'
class TecnicaAtaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicaAtaque
        fields = '__all__'
class TecnicaCurativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicaCurativa
        fields = '__all__'
class NinjaTecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NinjaTecnica
        fields = '__all__'
class NinjaMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NinjaMedico
        fields = '__all__'
class BestiaMiticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestiaMitica
        fields = '__all__'
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
class MisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mision
        fields = '__all__'
class EquipoEnMisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoEnMision
        fields = '__all__'
class PergaminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergamino
        fields = '__all__'
class EquipoEnMisionPergaminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoEnMisionPergamino
        fields = '__all__'
class BestiaMisionPergaminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestiaMisionPergamino
        fields = '__all__'
