# teniendo en cuenta el punto 2 se requiere tener el registro de 20 estudantes y poder determinar el estado de salud de la comunidad estudiantil
#el programa de be mostrar el siguiente reporte:
# estudiantes en pso ideal
#estudiantes en oesidad grado 1
#estudiantes en obesidad grado 2
#estudiantes en obesidad grado 3
#estudiantes en sobrepeso

import os
import art

flaco = 0
pi = 0
ob1 = 0
ob2 = 0
ob3 = 0
sp = 0
i = 1
art.tprint('Calciuladora de IMC')


while i <= 20:
    print('Estudiante numero: ', i)
    nombre = str(input('Hola bienvenido, ingrese su nombre: '))
    print(nombre, ' Cuantos años tienes? ')
    edad = int(input('_'))
    print(nombre, ' Cuanto mides? (cm) ')
    altura = int(input('_'))
    altura = altura/100
    print(nombre, ' Cuanto pesas? ')
    peso = int(input('_'))

    imc = peso / (altura * altura)

    os.system("cls")

    art.tprint('Resultados')
    print (nombre)

    if imc < 18.4:
        print('Estas muy flaco, come alguito')
        flaco = flaco + 1

    if imc > 18.5 and imc < 24.9:
        print ('tienes un IMC Normal')
        pi = pi + 1

    if imc > 25 and imc < 29.9:
        print ('tienes Sobrepeso')
        sp = sp + 1

    if imc > 30 and imc < 34.9:
        print ('tienes Obesidad I')
        ob1 = ob1 + 1

    if imc > 35 and imc < 39.9:
        print ('tienes Obesidad II')
        ob2 = ob2 + 1

    if imc > 40:
        print ('tienes Obesidad III')
        ob3 = ob3 + 1

    os.system("Pause")
    os.system("cls")
    
    i = i + 1

art.tprint("Conclusiones:")
print('Numero de estudiantes con Desnutricion: ', flaco)
print('Numero de estudiantes con IMC Normal: ', pi)
print('Numero de estudiantes con Sobrepeso: ', sp)
print('Numero de estudiantes con Obesidad I: ', ob1)
print('Numero de estudiantes con Obesidad II: ', ob2)
print('Numero de estudiantes con Obesidad III: ', ob3)
print('Fin del programa.')





