import tabulate
# Diccionario con los fundamentos de las rutas de entrenamiento
fundamentos = {
    'primera ruta': {
        'nombre': 'Node JS',
        'fundamentos': ['Introducción a la algoritmia', 'PSeInt', 'Python'],
        'Programación Web': ['HTML', 'CSS', 'Bootstrap'],
        'Programación formal': ['Java', 'JavaScript', 'C#'],
        'Bases de datos': ['Mysql', 'MongoDb', 'Postgresql'],
        'Backend': ['NetCore', 'Spring Boot', 'NodeJS', 'Express']
    },
    'segunda ruta': {
        'nombre': 'Java',
        'fundamentos': ['Introducción a la algoritmia', 'PSeInt', 'Python'],
        'Programación Web': ['HTML', 'CSS', 'Bootstrap'],
        'Programación formal': ['Java', 'JavaScript', 'C#'],
        'Bases de datos': ['Mysql', 'MongoDb', 'Postgresql'],
        'Backend': ['NetCore', 'Spring Boot', 'NodeJS', 'Express']
    },
    'tercera ruta': {
        'nombre': 'NetCore',
        'fundamentos': ['Introducción a la algoritmia', 'PSeInt', 'Python'],
        'Programación Web': ['HTML', 'CSS', 'Bootstrap'],
        'Programación formal': ['Java', 'JavaScript', 'C#'],
        'Bases de datos': ['Mysql', 'MongoDb', 'Postgresql'],
        'Backend': ['NetCore', 'Spring Boot', 'NodeJS', 'Express']
    }
}
headers = ['Ruta', 'Nombre', 'Fundamentos', 'Programación Web', 'Programación formal', 'Bases de datos', 'Backend']
rows = []
print(tabulate.tabulate(rows, headers=headers, tablefmt='grid'))

from registro_camper import campers
def asignar_camper_ruta():
        id_camper = input("Ingrese el ID del camper: ")
    
   
        if id_camper in campers:
            print("El ID del camper está registrado.")
            return
       

        

def entrena(rutas: dict):
    headers = ['Ruta', 'Nombre', 'Fundamentos', 'Programación Web', 'Programación formal', 'Bases de datos', 'Backend']
    rows = []

    for ruta, detalles in fundamentos.items():
        row = [ruta, detalles['nombre']]
        for tipo, tecnologias in detalles.items():
            if tipo != 'nombre':
                row.append(', '.join(tecnologias))
        rows.append(row)

    print(tabulate.tabulate(rows, headers=headers, tablefmt='grid'))
    id_camper = input("Ingrese el ID del camper: ")
    rta=print('ingrese  la ruta de entrenamiento que desea asignar(nodejs, java o netcore ): ')
    if rta == 'node js'.lower():
        campers.campers[id_camper]['Ruta'] = 'Node JS'
        print(f"El camper con ID {id_camper} ha sido asignado a la ruta Node JS.")
    elif rta == 'java'.lower :
        campers.campers[id_camper]['Ruta'] = 'Java'
        print(f"El camper con ID {id_camper} ha sido asignado a la ruta Java")   
    elif rta == 'net core'.lower():
        campers.campers[id_camper]['Ruta'] = 'NetCore'
        print(f"El camper con ID {id_camper} ha sido asignado a la ruta NetCore")
    else:
        print("El ID del camper no está registrado.")

    # Aquí puedes continuar con la lógica para las otras rutas, si es necesario.


# Llamada a la función entrena con el diccionario rutas
entrena(fundamentos)


