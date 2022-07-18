from rest_framework import status
from rest_framework.response import Response

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


def get_post(request, clase, serializador):
    print(request.data)
    print(clase)
    if request.method == 'GET':
        objects = clase.objects.all()
        serializer = serializador(objects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if Ninja==clase or Persona==clase or Jounin==clase or NinjaMedico==clase or Chunin==clase or Genin==clase:
            print("estoy aqui")
            print(request.data['id'])
            try:
                file = open("file.txt", "w")
                file.write(str(request.data["id"]))
                file.close()
            except Exception as e:
                print(e)
        serializer = serializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_put_delete(request, pk, clase, serializador):
    try:
        if BestiaMisionPergamino==clase:
            objeto = clase.objects.get(bestia=pk)
            print(objeto)
        elif Equipo==clase:
            objeto = clase.objects.get(ninja1_id=pk)
            print(objeto)
        elif EquipoEnMision==clase:
            objeto = clase.objects.get(equipo=pk)
            print(objeto)
        elif EquipoEnMisionPergamino==clase:
            objeto = clase.objects.get(equipoenmision=pk)
            print(objeto)
        elif NinjaTecnica==clase:
            objeto = clase.objects.get(ninja=pk)
            print(objeto)
        else:
            objeto = clase.objects.get(id=pk)
            print(objeto)
    except Exception as e:
        raise e
    if request.method == 'GET':
        serializer = serializador(objeto, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #instance=task
        serializer = serializador(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

