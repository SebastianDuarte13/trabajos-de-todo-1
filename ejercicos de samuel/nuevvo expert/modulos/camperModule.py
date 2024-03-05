def AddCamper(campers:dict):
    header = """
    *************************************
    *       MATRÍCULA DE CAMPERS        *
    *************************************
    """
    print(header)
    id = input('Ingrese el Id: ')
    nombre = input('Ingrese el Nombre: ')
    apellido = input('Ingrese el Apellido: ')
    direccion = input('Ingrese la Direccion: ')
    estado = 'Inscrito'
    tel = input('Ingrese el Telefono: ')
    camper = {
        'id':id,
        'nombre':nombre,
        'apellido':apellido,
        'direccion':direccion,
        'estado':estado,
        'tel':tel,
    }
    campers.update({id:camper})

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