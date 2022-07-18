from app.repository import helpers 

def get_headers(data):
    headers = helpers.get_headers(data)
    return headers

def get_records(data):
    model = helpers.get_model(data)
    records = model.objects.all()
    return records

def get_record(data, id):
    model = helpers.get_model(data)
    record = model.objects.get(pk=id)
    return record

def exist_model(data):
    return helpers.exist_model(data)

def get_types(data):
    return helpers.get_types(data)

def get_pointers(data):
    return helpers.get_pointers(data)
        
def get_all_pk(data):
    records = get_records(data)
    pks = []
    for record in records:
        pks.append(record.pk)
    return pks

def create_element(data,values):
    model = helpers.get_model(data)
    record = model()
    record.add_values(values)
    record.save_element()

def edit_element(data,id,values):
    record = get_record(data, id)
    record.add_values(values)
    record.save_element()

def delete_element(data, id):
    model = helpers.get_model(data)
    record = model.objects.get(pk=id)
    record.delete()
    
