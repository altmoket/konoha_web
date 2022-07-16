from app.repository import helpers 

def get_headers(data):
    headers = helpers.get_headers(data)
    return headers

def get_records(data):
    model = helpers.get_model(data)
    records = model.objects.all()
    return records

def exist_model(data):
    return helpers.exist_model(data)
        
