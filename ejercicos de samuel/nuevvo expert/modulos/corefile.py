import os
import json

DATABASE_FILE = ""

def update_file(*param):
    with open(DATABASE_FILE, "w") as wf:
        json.dump(param[0], wf, indent=4)

def add_data(*param):
    with open(DATABASE_FILE, "r+") as rwf:
        data_file = json.load(rwf)
        if len(param) > 1:
            data_file.update({param[0]: param[1]})
        else:
            data_file.update({param[0]})
        rwf.seek(0)
        json.dump(data_file, rwf, indent=4)
        rwf.close()

def eliminar(*param):
    data = list(param)
    data[1].pop(data[0])
    update_file(data[1])

def read_file():
    with open(DATABASE_FILE, "r") as rf:
        return json.load(rf)

def check_file(*param):
    data = list(param)
    if os.path.isfile(DATABASE_FILE):
        if len(param):
            data[0].update(read_file())
    else:
        if len(param):
            update_file(data[0])