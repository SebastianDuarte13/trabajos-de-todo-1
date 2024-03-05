import os
import tabulate

def reg_entrenadores(registro: list):
    titulo = """
    *************************************
    *     REGISTRO DE ENTRENADORES      *
    *************************************
    """
    print(titulo)
    
    while True:
        id_trainer = input("Ingrese ID del Trainer: ")
        nombre = input("Ingrese nombre del Trainer: ")
        apellido = input("Ingrese apellidos del Trainer: ")
        horario = input("Ingrese horario del Trainer (Día o Tarde): ")
        
        entrenador = {
            "NroId": id_trainer,
            "Nombre": nombre,
            "Apellidos": apellido,
            "Horario": horario,
            "RutasAsignadas": 0
        }
        
        registro.append(entrenador)
        
        otro = input(('¿Quieres ingresar otro entrenador? (si/no): ')).lower()
        if otro == 'no':
            os.system('cls')   
            break
        elif otro != 'si':
            print('Opción no válida')
            os.system('pause')
            os.system('cls')
        
    os.system('cls')  
    print("Registro de Entrenadores:")
    print(tabulate.tabulate([entrenador.values() for entrenador in registro], headers=registro[0].keys()))

# Crea una lista vacía para almacenar los entrenadores
registro_entrenadores = []
reg_entrenadores(registro_entrenadores)

