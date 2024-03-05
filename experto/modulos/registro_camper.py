import tabulate
import os

id_del_camper = set()  

def campers(registro: dict):
    cantidad_campers = 0  
    while True:
        titulo="""
        ************************
        *  registro de camper  *
        ************************
        """
        print(titulo)
        id_camper = input("Ingrese el ID del camper: ")
        nombre = input("Ingrese el Nombre del Camper: ")
        apellido = input("Ingresa los Apellidos del Camper: ")
        direccion = input("Ingrese la Dirección del Camper: ")
        acudiente = input("Ingrese el nombre del acudiente: ")
        telefono = input("Ingrese el Teléfono del Camper: ")

        registro_campers = {
            'ID': id_camper,
            'Nombre': nombre,
            'Apellido': apellido,
            'Dirección': direccion,
            'Acudiente': acudiente,
            'Teléfono': telefono,
            'Estado': 'inscrito'
        }

        registro[id_camper] = registro_campers
        id_del_camper.add(id_camper)  
        cantidad_campers += 1  

        os.system('cls')
        print("Registro de Campers:")
        print(tabulate.tabulate(registro.values(), headers='keys'))

        otro = input(('¿Quieres ingresar otro camper? (si/no): ')).lower()
        if otro == 'no':
            os.system('cls')
            break
        elif otro != 'si':
            print('Opción no válida')

        os.system('pause')
        os.system('cls')

    print(f"Se registraron {cantidad_campers} campers.")  

def buscar_camper(registro: dict):
    id_camper = input("Digite el ID del camper a buscar: ")
    data = registro.get(id_camper)
    if data:
        os.system('cls')
        print("Detalles del Camper:")
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Camper no encontrado en el registro.")

campers_registrados = {}
campers(campers_registrados)

#print(campers({}))
