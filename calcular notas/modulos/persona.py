import art
import os
import tabulate

def proceso():
    art.tprint('BIENVENIDO_USUARIO')
    dicc={1:'nombre', 2: 'examen teorico', 3:'examen practico',4:'tabla total'}
    calificaciones = {'nombre': '', 'examen teorico': 0, 'examen practico': 0}
    for key in dicc:
        print(key, dicc[key])
    eviden=True
    while  eviden:
        opcion = int(input('Ingresa una la opcion: '))
        if opcion==1:
            os.system('cls')
            nombre=input("Ingrese su nombre completo")
            calificaciones['nombre'] = nombre
        elif opcion ==2:
            os.system('cls')
            examen_teorico=float(input("Ingrese la calificacion del examen teorico"))
            calificaciones['examen teorico'] = examen_teorico
        elif opcion==3 :
            os.system('cls')
            examen_practico=float(input("Ingrese la calificacion del examen practico"))
            calificaciones['examen practico'] = examen_practico
        elif opcion==4:
            os.system('cls')
            print(tabulate([(calificaciones['nombre'], calificaciones['examen teorico'], calificaciones['examen practico'])], headers=['Nombre', 'Examen Teorico', 'Examen Practico'], tablefmt='pretty'))
            eviden=False
        else:
            print("Opcion no valida")

proceso()
    

   
