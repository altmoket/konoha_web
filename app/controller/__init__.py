
from datetime import datetime
from app import repository
from app.forms import FormCreator

def get_headers(data):
    headers = repository.get_headers(data)
    return headers

def get_records(data):
    records = repository.get_records(data)
    return records

def exist_model(data):
    return repository.exist_model(data)

def get_types(data):
    return repository.get_types(data)

def get_pointers(data):
    return repository.get_pointers(data)

def get_names(data):
    headers = list(get_headers(data))
    headers.pop(0)
    return headers

def get_options(data):
    types = repository.get_types(data)
    pointers = repository.get_pointers(data)
    options = []
    for i in range(len(types)):
        if types[i] == 'Select':
            pks = repository.get_all_pk(pointers[i])
            options.append(pks)
        elif types[i] == 'Choices':
            options.append(pointers[i])
        else:
            options.append('')
    return options

def create_element(data, values):
    types = get_types(data)
    for i in range(len(types)):
        if types[i] == 'Int' or types[i] == 'Select':
            values[i] = int(values[i])
        elif types[i] == 'Boolean':
            if values[i] == 'True':
                values[i] = True
            else:
                values[i] = False
        elif types[i] == 'Date':
            fecha = datetime.strptime(values[i], '%Y-%m-%d')
            values[i] = fecha
    repository.create_element(data,values)
    
    
def create_form(data):
    headers = get_headers(data)
    types = repository.get_types(data)
    pointers = repository.get_pointers(data)
    options = []
    for i in range(len(types)):
        if types[i] == 'Select':
            pks = repository.get_all_pk(data)
            options.append(pks)
        elif types[i] == 'Choices':
            options.append(pointers[i])
        else:
            options.append('')
    form = FormCreator(data,headers,types,options)
    return form
