from email import header
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}

    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
        'name':'bakib',
        'roll':18,
        'city':'Satkhira'
    }

    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers,data=json_data)
    data = r.json()
    print(data)

def update_data():
    data = {
        'name':'MMM',
        'id':9,
        'roll':33,
        'city':'Satkhira'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

def delete_data():
    data = {
        'id':10  
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)


delete_data()
# update_data()
# get_data()
# post_data()