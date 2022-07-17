
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from app import controller


def home(request):
    return render(request, 'home.html', { 'selected': 'Persona'})

def listar(request):
    if request.method == 'GET':
        data = str(request.GET['data'])
        if controller.exist_model(data):
            headers = controller.get_headers(data)
            records = controller.get_records(data)
            return render(request, 'listar.html', {'data':data, 'headers':headers, 'records': records, 'selected':data})
    return home(request)
@api_view(['POST'])
def agregar_elemento(request):
    all_values = request.POST
    data = request.POST['data']
    names = controller.get_names(data)
    values = []
    for name in names:
        values.append(all_values[name])
    controller.create_element(data, values)
    return redirect('/app/listar?data='+data) 
@api_view(['GET'])
def agregar(request, data):
    if controller.exist_model(data):
        names = controller.get_names(data)
        types = controller.get_types(data)
        options = controller.get_options(data)
        lista_conjunta = zip(names,types,options)
        return render(request, 'agregar.html', {'data':data, 'lista_conjunta':lista_conjunta, 'selected':data})
    return home(request)
@api_view(['GET'])
def editar(request, data, pk):
    if controller.exist_model(data):
        names = controller.get_names(data)
        types = controller.get_types(data)
        options = controller.get_options(data)
        record = controller.get_record_in_array(data, pk)
        pk = record.pop(0)
        lista_conjunta = zip(names,types,options,record)
        return render(request, 'editar.html', {'data':data, 'lista_conjunta':lista_conjunta, 'selected':data, 'pk':pk})
    return home(request)
@api_view(['PUT'])
def editar_elemento(request):
    pass

@api_view(['GET'])
def eliminar_elemento(_, data, pk):
    controller.delete_element(data, pk)
    return redirect('/app/listar?data='+data) 
