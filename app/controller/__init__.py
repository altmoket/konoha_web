from datetime import datetime
from app import repository
from app.controller import helpers

def get_headers(data):
    headers = repository.get_headers(data)
    return headers

def get_records(data):
    records = repository.get_records(data)
    return records

def get_record(data, pk):
    record = repository.get_record(data, pk)
    return record

def get_record_in_array(data, pk):
    record = get_record(data, pk)
    attributes = []
    for attribute in record:
        attributes.append(attribute) 
    return attributes

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

def get_model(data):
    return repository.get_model(data)

def get_serializer(data):
    return helpers.get_serializer(data)

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
    pointers = get_pointers(data)
    for i in range(len(types)):
        if types[i] == 'Int':
            values[i] = int(values[i])
        elif types[i] == 'Boolean':
            if values[i] == 'True':
                values[i] = True
            else:
                values[i] = False
        elif types[i] == 'Date':
            fecha = datetime.strptime(values[i], '%Y-%m-%d')
            values[i] = fecha
        elif types[i] == 'Select':
            pk = int(values[i])
            record = repository.get_record(pointers[i], pk)
            values[i] = record
    repository.create_element(data,values)

def edit_element(data, values):
    pk = values.pop(0)
    types = get_types(data)
    pointers = get_pointers(data)
    for i in range(len(types)):
        if types[i] == 'Int':
            values[i] = int(values[i])
        elif types[i] == 'Boolean':
            if values[i] == 'True':
                values[i] = True
            else:
                values[i] = False
        elif types[i] == 'Date':
            fecha = datetime.strptime(values[i], '%Y-%m-%d')
            values[i] = fecha
        elif types[i] == 'Select':
            pk = int(values[i])
            record = repository.get_record(pointers[i], pk)
            values[i] = record
    repository.edit_element(data,pk,values)

def delete_element(data, pk):
    repository.delete_element(data,pk)
