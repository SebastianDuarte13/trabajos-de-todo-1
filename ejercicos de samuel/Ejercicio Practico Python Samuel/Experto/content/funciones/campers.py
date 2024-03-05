import json
import funciones.corefile as cf

cf.MY_DATABASE = 'data/campers.json'
def NewCamper(campus : dict):
    data=campus.get("campus").get("campers")
    Camper={
        "NroId":"",
        "NroId":"",
        "Nombre":"",
        "Apellido":"",
        "Direccion":"",
        "Acudiente" :{},
        "telecontacto" : {},
        "estado":""
    }
    acudiente={
        "id":"1",
        "nrotel":"6666",
        "nombre":"acudiente1",
        "email":"acuentiente@gmail.com"
    }
    phone ={
        "id":"1",
        "nrotel":"444",
        "ubicacion":"casa",
    }
    Camper1 = {
        "NroId":"123",
        "Nombre":"BBB",
        "Apellido":"AAA",
        "Direccion":"Cra",
        "Acudiente" :{},
        "telecontacto" : {},
        "estado":"I"    
    }   

    Camper1["Acudiente"].update({str(len(Camper1["Acudiente"])+1).zfill(3):acudiente})
    data.update({Camper1["NroId"]:Camper1})
    campus.get("campus").get("campers").update(data)
    print(json.dumps(campus,indent=4))
    # clientes.update(customer)
    # cf .AddData(customer[ "cc" ], clientes)

