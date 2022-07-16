
from django.http import HttpResponseRedirect
from django.shortcuts import render
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

def agregar(request):
    if request.method == 'GET':
        data = str(request.GET['data'])
        if controller.exist_model(data):
            return render(request, 'agregar.html', {'data':data})
    return home(request)
