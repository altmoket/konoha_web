from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.helpers import get_post, get_put_delete
from django.shortcuts import render
from api.models.Persona import Persona
from api.serializers.PersonaSerializer import PersonaSerializer
from api.controllers.PersonaControlador import PersonaControlador

#personas
@api_view(['GET','POST'])
def persona_list(request):
    return get_post(request, Persona, PersonaSerializer)
@api_view(['GET','PUT','DELETE'])
def persona_detail(request,pk):
    return get_put_delete(request, pk, Persona, PersonaSerializer)

@api_view(['GET'])
def listar_personas(request):
    return Response(PersonaControlador.listar())

@api_view(['POST'])
def crear_persona(request):
    pass

@api_view(['PUT'])
def actualizar_persona(request, pk):
    pass

@api_view(['GET'])
def mostrar_persona(request, pk):
    pass

@api_view(['DELETE'])
def eliminar_persona(request, pk):
    pass
