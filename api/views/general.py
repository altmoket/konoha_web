
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import helpers

from app import controller


@api_view(['GET','POST'])
def get_post(request, data=""):
    if request.method == 'POST':
        data = request.POST['data']
    model = controller.get_model(data)
    serializer = controller.get_serializer(data)
    return helpers.get_post(request, model, serializer)

@api_view(['GET','PUT','DELETE'])
def get_put_delete(request, data, pk):
    model = controller.get_model(data)
    serializer = controller.get_serializer(data)
    return helpers.get_put_delete(request, pk, model, serializer)

@api_view(['GET'])
def index(request, data):
    records = controller.get_records(data)
    headers = controller.get_headers(data)
    lista = zip(headers, records)
    result = []
    for record in records:
        element = {}
        lista = zip(headers, record)
        for header,attribute in lista:
            element.__setitem__(header,attribute)
        result.append(element)
    return Response(result)

@api_view(['POST'])
def create(request):
    data = request.POST['data']
    model = controller.get_model(data)
    serializer = controller.get_serializer(data)
    return get_post(request, model, serializer)

@api_view(['PUT'])
def edit(request, pk):
    pass

@api_view(['DELETE'])
def delete(request, pk):
    pass

@api_view(['GET'])
def watch(request, data, pk):
    pass
    
    

