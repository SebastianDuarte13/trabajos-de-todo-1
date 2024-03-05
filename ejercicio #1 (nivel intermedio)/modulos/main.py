import os
import art
from ciudades import *
ciudades_reg=[]
def menu():
    while True:
        art.tprint('centro de prevencion de sismos')
        titulo="""
        ++++++++++++++++++++
        +  Menu principal  +
        ++++++++++++++++++++
        """
        print(titulo)
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar sismos por ciudad")
        print("4. Informe de riesgo")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registro_ciudades(ciudades_reg)
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


