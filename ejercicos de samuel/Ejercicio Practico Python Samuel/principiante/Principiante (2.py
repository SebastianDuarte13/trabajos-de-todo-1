#realizar un programa que calcule el imc de los estudiantes nuevos.
#imc = peso / altura al cuadrado
#el programa debe mostrar el nombre del estudiante, la edad, el imc y las categorias segun el imc obtenido
#normal = imc entre 18.5 - 24.9
#sobrepeso imc entre 25 - 29.9
#obesidad 1 = imc 30 - 34.9
#obesidad 2 = imc 35 - 39.9
#obesidad 3 = imc > 40

import art, os

art.tprint('Calciuladora de IMC')

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

if imc > 18.5 and imc < 24.9:
    print ('tienes un IMC Normal')

if imc > 25 and imc < 29.9:
    print ('tienes Sobrepeso')

if imc > 30 and imc < 34.9:
    print ('tienes Obesidad I')

if imc > 35 and imc < 39.9:
    print ('tienes Obesidad II')

if imc > 40:
    print ('tienes Obesidad III')
