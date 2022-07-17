
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from app import controller

from app.forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/app/thanks/')
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

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
def agregar_view(request, data):
    if request.method == 'GET':
        if controller.exist_model(data):
            names = controller.get_names(data)
            types = controller.get_types(data)
            options = controller.get_options(data)
            lista_conjunta = zip(names,types,options)
            return render(request, 'agregar.html', {'data':data, 'lista_conjunta':lista_conjunta, 'selected':data})
    return home(request)

@api_view(['GET'])
def eliminar_elemento(_, data, pk):
    controller.delete_element(data, pk)
    return redirect('/app/listar?data='+data) 
