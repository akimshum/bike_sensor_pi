import json
import datetime
import os

FOLDER_DATA = os.path.expanduser('~')+'/data-bike/'


def get_all_filenames():
    return os.listdir(FOLDER_DATA)


def generate_name_file():
    now = datetime.datetime.now().timestamp()
    return FOLDER_DATA + str(now) + '.json'


def read_json(file_name):
    with open(FOLDER_DATA + file_name, 'r') as openfile:
        return json.load(openfile)


def save_json(data):
    if not os.path.exists(FOLDER_DATA):
        os.makedirs(FOLDER_DATA)
    with open(generate_name_file(), "w") as outfile:
        json.dump(data, outfile)


def delete_json(file_name):
    os.remove(FOLDER_DATA + file_name)
