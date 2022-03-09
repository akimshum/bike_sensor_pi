from cmath import log
import requests
import json
from file_manager import manager

URL_UPLOAD_DATA = 'http://192.168.178.103:5000/bike'

file_names = manager.get_all_filenames()

try:
    for filename in file_names:
        if(filename.__contains__('.json')):
            print(filename)
            data = manager.read_json(filename)
            print(data)
            response = requests.post(
                URL_UPLOAD_DATA, data=json.dumps(data), headers={'content-type': 'application/json'})
            print(response.text)
            if(response.status_code == 200):
                manager.delete_json(filename)
except Exception as e:
    print('Error:' + e)
