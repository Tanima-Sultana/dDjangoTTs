import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if data is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
        'name':'bkib',
        'roll':10,
        'city':'Satkhira'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

def update_data():
    data = {
        'name':'MMM',
        'id':4,
        'roll':33,
        'city':'Satkhira'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

def delete_data():
    data = {
        'id':5  
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


delete_data()
# update_data()
# get_data()
# post_data()