import json
import funciones.campers as c 

mi_campus ={
    "campus":{
        "campers":{},
        "rutas":{},
        "pruebas":{},  
        "salones":{},
        "entrenadores":{}  
    }
}

if __name__ == "__main__":
    c.new_camper(mi_campus)
    
