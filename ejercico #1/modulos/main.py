import os
from menu import*
def menu():
    os.system('cls')
    art.tprint('BIENVENIDOS A LA LIGA BETPLAY')
    for key in diccionario:
        print(key, diccionario[key])
    opcion = int(input('Ingresa una la opcion: '))
    if opcion == 1:
        os.system('cls')
        agregar_equipo()
    elif opcion == 2:
        pass  # agregar fecha
    elif opcion == 3:
        pass  # tabla de posiciones
    elif opcion == 4:
        pass  # reportes
    elif opcion == 5:
        print('Saliendo del programa...')
        os.system('pause')
        return False
    else:
        print('Opción incorrecta')
        os.system('pause')
    return True

condici = True
while condici:
    condici = menu()