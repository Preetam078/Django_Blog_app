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

#get_data(1)
#get_dataParams()


#function to add data
def post_data():
    data = {
         'name':'ravi',
         'roll':11,
         'city':'raipur'
    }
    
    json_data = json.dumps(data)
    req = requests.post(url = URL, data=json_data)
    res = req.json()
    print(res)


#post_data()

#update the data
def update_data():
    data = {
         'id':1,
         'name':'raja mundru',
         'roll':12,
         'city':'chennai'
    }
    
    json_data = json.dumps(data)
    req = requests.put(url = URL, data=json_data)
    res = req.json()
    print(res)

#update_data()``

#Delete the data
def delete_data():
    data = {'id':1}
    
    json_data = json.dumps(data)
    req = requests.delete(url = URL, data=json_data)
    res = req.json()
    print(res)

delete_data()