#La mala para criatian
#La mala para sebastian
#se requiere realizar4 un programa que permita leer 3 numeros enteros positivos e imprime la sumatoria de los 3 numeros

import art
import os
art.tprint('Calculadora')

num1 = 0
num2 = 0
num1 = 0

num1 = int(input('Ingresa el primer numero a sumar: '))
while num1 < 0:
    print('el numero ingresado no es valido, debe ser positivo')
    num1 = input('ingresa un numero nuevo: ')

num2 = int(input('Ingresa el segundo numero a sumar: '))
while num2 < 0:
    print('el numero ingresado no es valido, debe ser positivo')
    num2 = input('ingresa un numero nuevo: ')

num3 = int(input('Ingresa el tercer numero a sumar: '))
while num3 < 0:
    print('el numero ingresado no es valido, debe ser positivo')
    num3 = input('ingresa un numero nuevo: ')

resultado = num1 + num2 + num1

os.system("cls")

art.tprint('Resultados')
print('La suma de los numeros:', num1,', ',num2,', ',num3,' Es: ',resultado)
  
