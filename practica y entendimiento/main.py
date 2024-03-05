import ciudades
import sismos
import os
import art
def main():
    ciudades_registradas = []
    while True:
        art.tprint('centro de prevencion de sismos')
        titulo="""
        ++++++++++++++++++++
        +  Menu principal  +
        ++++++++++++++++++++

        """
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar sismos por ciudad")
        print("4. Informe de riesgo")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ciudades.registro(ciudades_registradas)
            os. system('pause')
            os. system('cls')
        elif opcion == "2":
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
            ciudad = ciudades.buscar(ciudades_registradas, nombre_ciudad)
            if ciudad:
                sismos.registrar_sismo(ciudad)
                os.system('pause')
                os.system('cls')
            else:
                print("Ciudad no encontrada.")
                os. system('pause')
                os. system('cls')
        elif opcion == "3":
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
            ciudad = ciudades.buscar_ciudad(ciudades_registradas, nombre_ciudad)
            if ciudad:
                print(f"Sismos registrados en {nombre_ciudad}:")
                print(ciudad["sismos"])
                os.system('pause')
                os.system('cls')
            else:
                print("Ciudad no encontrada.")
                os.system('pause')
                os.system('cls')
        elif opcion == "4":
            for ciudad in ciudades_registradas:
                promedio_sismos = sismos.calcular_promedio_sismos(ciudad)
                riesgo = sismos.generar_informe_riesgo(promedio_sismos)
                print(f"Informe de riesgo para la ciudad {ciudad['nombre']}: {riesgo}")
                os.system('pause')
                os.system('cls')
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
