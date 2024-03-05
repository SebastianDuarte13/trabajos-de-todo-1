import modulos.areassalones as salones
import modulos.pruebas as pruebas
import modulos.camperModule as campers
import modulos.corefile as corefile

lista_modulos = ["Fundamentos de programacion", "Programacion Web", "Programacion Formal", "Bases de Datos", "Backend"]

def crear_ruta(campus: dict):
    header = """
    *************************************
    *        CREACIÓN DE RUTAS          *
    *************************************
    """
    print(header)
    global is_incomplete
    is_incomplete = True
    data_rutas = campus.get("campus").get("rutas")
    data_entrenadores = campus.get("campus").get("entrenadores")
    nombre = ""
    valor = 0
    
    while nombre == "":
        nombre = input("Ingrese el nombre de la ruta: ")
    id_salon = salones.buscar_salon(campus)
    if id_salon != "":
        id_trainer = campers.verificar_dato(valor, "Ingrese el id del entrenador: ", data_entrenadores)
        if data_entrenadores.get(id_trainer)["RutasAsignadas"] < 2:
            ruta = {
                "NroId": str(len(campus["campus"]["rutas"]) + 1),
                "Nombre": nombre,
                "modulos": {},
                "IdSalon": id_salon,
                "IdTrainer": id_trainer
            }
            for i, item in enumerate(lista_modulos):
                modulo = {
                    "Id": str(i + 1),
                    "Nombre": item,
                    "Temas": []
                }
                print(f"")
                print(f"Módulo {item}".upper())
                print(f"")
                valor = 0
                rta = 2
                j = 1
                while j <= rta:
                    tema = input("Ingrese el nombre del tema correspondiente al módulo: ")
                    if tema != "":
                        modulo["Temas"].append(tema)
                        j = j + 1
                    else:
                        print("El tema no puede estar vacío")
                ruta["modulos"].update({modulo["Id"]: modulo})
            data_rutas.update({ruta["NroId"]: ruta})
            data_entrenadores.get(id_trainer).update({"RutasAsignadas": data_entrenadores.get(id_trainer)["RutasAsignadas"] + 1})
            campus.get("campus").get("rutas").update(data_rutas)
            campus.get("campus").get("entrenadores").update(data_entrenadores)
            corefile.UpdateFile(campus)
        else:
            print("No se le pueden asignar más rutas a este entrenador")
    else:
        print("No se puede crear una ruta sin un salón")

def buscar_ruta(campus: dict) -> str:
    id_ruta = ""
    while id_ruta == "":
        id_ruta = input("Ingrese el id de la ruta: ")
    data = campus.get("campus").get("rutas").get(id_ruta, -1)
    if type(data) == dict:
        return id_ruta
    else:
        print("No existe una ruta con este código")
        return ""
    
def mostrar_ruta(id_ruta: str, campus: dict):
    print(f"")
    print(f"RUTA")
    print(f"")
    data_ruta = campus.get("campus").get("rutas").get(id_ruta, -1)
    data_campers = campus.get("campus").get("campers").keys()
    data_entrenador = campus.get("campus").get("entrenadores").get(data_ruta["IdTrainer"], -1)
    print(f"\tCAMPERS")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    for i in list(data_campers):
        data_camper = campus.get("campus").get("campers").get(i, -1)
        if "idRuta" in data_camper and data_camper["idRuta"] == id_ruta:
            print("{:<15} {:<15} {:<20}".format(data_camper["NroId"], data_camper["Nombre"], data_camper["Apellido"]))
    print(f"")
    print(f"\tENTRENADOR")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    print("{:<15} {:<15} {:<20}".format(data_entrenador["NroId"], data_entrenador["Nombre"], data_entrenador["Apellidos"]))
