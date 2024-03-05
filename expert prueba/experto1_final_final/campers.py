import funciones.corefile as cf

MY_DATABASE = 'data/campus.json'
isEmpty = True

def verificarDato(valorDato, enunciadoDato, data) -> str:
    global isEmpty
    isEmpty = True
    valorDato = ""

    while isEmpty:
        valorDato = input(f"{enunciadoDato}")
        if valorDato != "":
            if enunciadoDato == "Ingrese ID del Camper : ":
                dataId = data.get(valorDato, -1)
                if type(dataId) == dict:
                    print(f"El ID ya se encuentra registrado")
                else:
                    isEmpty = False
            elif enunciadoDato == "Ingrese el id del trainer : ":
                dataId = data.get(valorDato, -1)
                if type(dataId) != dict:
                    print(f"El entrenador no se encuentra registrado")
                else:
                    isEmpty = False
            elif enunciadoDato in ["Ingrese el id de la ruta : ", "Ingrese el id de la ruta asociada con el Trainer : "]:
                dataId = data.get(valorDato, -1)
                if type(dataId) != dict:
                    print(f"La ruta no se encuentra registrada")
                else:
                    isEmpty = False
            elif enunciadoDato == "Ingrese el id del salón : ":
                dataId = data.get(valorDato, -1)
                if type(dataId) != dict:
                    print(f"El salón no se encuentra registrado")
                else:
                    isEmpty = False
            elif enunciadoDato == "Ingrese ID del Trainer : ":
                dataId = data.get(valorDato, -1)
                if type(dataId) == dict:
                    print(f"El ID ya se encuentra registrado")
                else:
                    isEmpty = False
            else:
                isEmpty = False
        else:
            print(f"El dato no puede estar vacío")

    return valorDato

def regCamper(campus: dict):
    header = """
    *************************************
    *       REGISTRO DE CAMPERS         *
    *************************************
    """
    print(header)
    data = campus.get("campus").get("campers")
    valor = ""

    print(f"")
    print(f"DATOS DEL CAMPER")
    print(f"")
    id_camper = verificarDato(valor, "Ingrese ID del Camper : ", data)
    nombre = verificarDato(valor, "Ingrese nombre del Camper : ", data)
    apellido = verificarDato(valor, "Ingrese apellidos del Camper : ", data)
    direccion = verificarDato(valor, "Ingrese direccion del Camper : ", data)
    nro_tel_cel = verificarDato(valor, "Ingrese teléfono celular del Camper : ", data)
    nro_tel_fijo = verificarDato(valor, "Ingrese teléfono fijo del Camper : ", data)
    ubicacion_tel_fijo = verificarDato(valor, "Ingrese si el teléfono pertenece a Casa o Trabajo : ", data)

    print(f"")
    print(f"DATOS DEL ACUDIENTE")
    print(f"")
    id_acudiente = verificarDato(valor, "Ingrese ID del acudiente del Camper : ", data)
    nro_tel_acudiente = verificarDato(valor, "Ingrese número de teléfono del acudiente del Camper : ", data)
    nombre_acudiente = verificarDato(valor, "Ingrese nombre del acudiente del Camper : ", data)
    email_acudiente = verificarDato(valor, "Ingrese email del acudiente del Camper : ", data)

    camper = {
        "NroId": id_camper,
        "Nombre": nombre,
        "Apellido": apellido,
        "Direccion": direccion,
        "Acudiente": {},
        "Telecontacto": {},
        "Estado": "Inscrito",
    }

    acudiente = {
        "id": id_acudiente,
        "nrotel": nro_tel_acudiente,
        "nombre": nombre_acudiente,
        "email": email_acudiente
    }

    phone_cel = {
        "id": str((len(camper["Telecontacto"]) + 1)),
        "nrotel": nro_tel_cel,
        "ubicacion": ""
    }

    phone_fijo = {
        "id": str((len(camper["Telecontacto"]) + 1)),
        "nrotel": nro_tel_fijo,
        "ubicacion": ubicacion_tel_fijo
    }

    camper["Acudiente"].update({str((len(camper["Acudiente"]) + 1)).zfill(3): acudiente})
    camper["Telecontacto"].update({str((len(camper["Telecontacto"]) + 1)).zfill(3): phone_cel})
    camper["Telecontacto"].update({str((len(camper["Telecontacto"]) + 1)).zfill(3): phone_fijo})
    data.update({camper["NroId"]: camper})
    campus.get("campus").get("campers").update(data)
    cf.UpdateFile(campus)

def buscarCamper(id_camper: str, campus: dict) -> dict:
    data = campus.get("campus").get("campers").get(id_camper, -1)
    if type(data) != dict:
        print(f"No se encontró un Camper con este código")
        return {}
    else:
        return data

def matricularCamper(campus: dict):
    header = """
    *************************************
    *       MATRÍCULA DE CAMPERS        *
    *************************************
    """
    print(header)
    data_r = campus.get("campus").get("rutas")
    data_s = campus.get("campus").get("salones")
    id_camper = ""

    while id_camper == "":
        id_camper = input(f"Ingrese el id del Camper que desea matricular : ")
    camper = buscarCamper(id_camper, campus)

    if camper != {} and camper["Estado"] == "Aprobado":
        valor = 0
        id_ruta = verificarDato(valor, "Ingrese el id de la ruta : ", data_r)
        id_salon = data_r.get(id_ruta)["IdSalon"]
        id_trainer = data_r.get(id_ruta)["IdTrainer"]
        if data_s.get(id_salon)["capacidad"] == 33:
            print(f"No se pueden agregar más Campers a esta ruta")
        else:
            fecha_inicio = verificarDato(valor, "Ingrese la fecha de inicio : ", camper)
            fecha_final = verificarDato(valor, "Ingrese la fecha final : ", camper)
            camper.update({"Estado": "Matriculado"})
            camper.update({"idRuta": id_ruta})
            camper.update({"idSalon": id_salon})
            camper.update({"idTrainer": id_trainer})
            camper.update({"fechaInicio": fecha_inicio})
            camper.update({"fechaFinal": fecha_final})
            data_s.get(id_salon).update({"capacidad": data_s.get(id_salon)["capacidad"] + 1})
            cf.UpdateFile(campus)
            print(f"")
            print(f"MATRICULA EXITOSA")
            print(f"")
    else:
        print(f"No se puede matricular")

def campersInscritos(campus: dict):
    print(f"")
    print(f"LISTADO DE CAMPERS INSCRITOS")
    print(f"")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    print(f"------------------------------------------------------")
    data = campus.get("campus").get("campers").keys()
    for i in list(data):
        data_c = campus.get("campus").get("campers").get(i, -1)
        if data_c["Estado"] == "Inscrito":
            print("{:<15} {:<15} {:<20}".format(data_c["NroId"], data_c["Nombre"], data_c["Apellido"]))

def campersAprobados(campus: dict):
    print(f"")
    print(f"LISTADO DE CAMPERS APROBADOS")
    print(f"")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    print(f"------------------------------------------------------")
    data = campus.get("campus").get("campers").keys()
    for i in list(data):
        data_c = campus.get("campus").get("campers").get(i, -1)
        if data_c["Estado"] == "Aprobado":
            print("{:<15} {:<15} {:<20}".format(data_c["NroId"], data_c["Nombre"], data_c["Apellido"]))

def campersBajoRendimiento(campus: dict):
    print(f"")
    print(f"LISTADO DE CAMPERS CON BAJO RENDIMIENTO")
    print(f"")
    print("{:<15} {:<15} {:<20}".format("ID", "NOMBRE", "APELLIDO"))
    print(f"------------------------------------------------------")
    data = campus.get("campus").get("campers").keys()
    for i in list(data):
        data_c = campus.get("campus").get("campers").get(i, -1)
        if data_c["Estado"] == "En Riesgo":
            print("{:<15} {:<15} {:<20}".format(data_c["NroId"], data_c["Nombre"], data_c["Apellido"]))