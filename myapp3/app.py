import requests
import json 

URL = 'http://127.0.0.1:8000/student/'
URL2 = 'http://127.0.0.1:8000/student/3'

def get_dataParams():

    req = requests.get(url = URL2)
    data = req.json()
    print(data)

  
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    req = requests.get(url = URL, data=json_data)
    reqdata = req.json()
    print(reqdata)

get_data(1)
#get_dataParams()
