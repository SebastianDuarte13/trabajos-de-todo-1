import funciones.campers as c
import funciones.corefile as cf

def reg_entrenadores(campus : dict):
    header = """
    *************************************
    *     REGISTRO DE ENTRENADORES      *
    *************************************
    """
    print(header)
    data_e = campus.get("campus").get("entrenadores")
    valor = ""
    
    id_trainer = c.verificarDato(valor, "Ingrese ID del Trainer : ", data_e)
    nombre = c.verificarDato(valor, "Ingrese nombre del Trainer : ", data_e)
    apellido = c.verificarDato(valor, "Ingrese apellidos del Trainer : ", data_e)
    horario = c.verificarDato(valor, "Ingrese horario del Trainer (Dia o Tarde) : ", data_e)
    
    entrenador = {
        "NroId" : id_trainer,
        "Nombre" : nombre,
        "Apellidos" : apellido,
        "Horario" : horario,
        "RutasAsignadas" : 0
    }

    data_e.update({entrenador["NroId"] : entrenador})
    campus.get("campus").get("entrenadores").update(data_e)
    cf.UpdateFile(campus)

def entrenadores_campus(campus : dict):
    print(f"")
    print(f"LISTADO DE ENTRENADORES")
    print(f"")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    print(f"------------------------------------------------------")
    data = campus.get("campus").get("entrenadores").keys()
    for i in list(data):
        data_e = campus.get("campus").get("entrenadores").get(i, -1)
        print("{:<15} {:<15} {:<20}".format(data_e["NroId"], data_e["Nombre"], data_e["Apellidos"]))