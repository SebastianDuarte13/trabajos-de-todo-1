import main
import art
import tabulate
import os

def main_menu():
    while True:
        art.tprint('BIENVENIDO')
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Camper")
        print("2. Registrar Prueba")
        print("3. Registrar Área de Entrenamiento")
        print("4. asignar Ruta de Entrenamiento")
        print("5. Asignar Camper a Ruta")
        print("6. registrar Entrenador a Ruta")
        print("7. reportes")
        print("8. Salir")
        
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            os.system('cls')
            import registro_camper as rc    
            rc.campers
        elif opcion == '2':
            os.system('cls')
            import registro_prueba as rp
        elif opcion == '3':
            os.system('cls')
            import areas_entrenamiento as ae
            ae.registrar_area_entrenamiento
        elif opcion == '4':
            os.system('cls')
            import rutas as r
            r.asignar_camper_ruta
            os.system('cls')
            r.entrena
        elif opcion == '5':
            os.system('cls')
            #import asignacion_camper_ruta as acr
        elif opcion == '6':
            os.system('cls')
            import registro_entrenadores as re
            re.reg_entrenadores
        elif opcion == '7':
            #rc.print(n
            pass
        elif opcion == '8':
            print("¡Hasta luego!")
            break
        else:
            os.system('cls')
            print("Opción no válida. Por favor, ingrese un número del 1 al 8.")

if __name__ == "__main__":
    main_menu()

            
#main.main_menu()

#alumnos=()#rg.campers(alumnos)
    
