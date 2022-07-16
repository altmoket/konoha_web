
from app import repository

def get_headers(data):
    headers = repository.get_headers(data)
    return headers

def get_records(data):
    records = repository.get_records(data)
    return records

def exist_model(data):
    return repository.exist_model(data)
    

