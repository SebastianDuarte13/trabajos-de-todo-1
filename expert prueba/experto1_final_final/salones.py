import funciones.corefile as corefile

is_empty = True

def verificar_dato(valor_dato, enunciado_dato, data) -> str:
    global is_empty
    is_empty = True
    valor_dato = ""
    while is_empty:
        valor_dato = input(f"{enunciado_dato}")
        if valor_dato != "":
            if enunciado_dato == "Ingrese el ID del salón : ":
                data_id = data.get(valor_dato, -1)
                if type(data_id) == dict:
                    print(f"El ID ya se encuentra registrado")
                else:
                    is_empty = False
            else:
                is_empty = False
        else:
            print(f"El dato no puede estar vacío")
    return valor_dato

def reg_salones(campus: dict):
    header = """
    *************************************
    *       REGISTRO DE SALONES         *
    *************************************
    """
    print(header)
    data = campus.get("campus").get("salones")
    valor = 0
    
    id_salon = verificar_dato(valor, "Ingrese el ID del salón : ", data)
    nombre = verificar_dato(valor, "Ingrese el nombre del salón : ", data)

    salon = {
        "id": id_salon,
        "nombre": nombre,
        "capacidad": 0
    }

    data.update({salon["id"]: salon})
    campus.get("campus").get("salones").update(data)
    corefile.UpdateFile(campus)

def buscar_salon(campus: dict) -> str:
    id_salon = input("Ingrese el ID del salón asignado : ")
    data = campus.get("campus").get("salones").get(id_salon, -1)
    if type(data) == dict:
        return id_salon
    else:
        print("No existe un salón con este código")
        return ""
