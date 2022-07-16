from rest_framework import status
from rest_framework.response import Response


def get_post(request, clase, serializador):
    if request.method == 'GET':
        objects = clase.objects.all()
        serializer = serializador(objects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_put_delete(request, pk, clase, serializador):
    try:
        objeto = clase.objects.get(id=pk)
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
