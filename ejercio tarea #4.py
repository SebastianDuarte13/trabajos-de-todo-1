import os
numeros = []
pares = []
impares = []

while True:
    numero = int(input("Ingrese un número entero positivo (ingrese un número negativo para terminar): "))
    if numero < 0:
        break
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

tn=len(numeros)
tp=len(pares)
ti=len(impares)

if tp > 0:
    pp = sum(pares) / tp
else:
    pp = 0

if ti > 0:
    pi = sum(impares) / ti
else:
    pi = 0

menores = sum(1 for num in numeros if num < 10)
entre = sum(1 for num in numeros if 20 <= num <= 50)
mayores = sum(1 for num in numeros if num > 100)

os.system('cls')
titulo="""
*********************
*      Reportes     *
*********************
"""
print(titulo)
print('la cantidad de numeros ingresados fueron: ', tn)
print(' Los pares ingresados fueron: ', tp)
print('El promedio de los pares fue: ', pp)
print('El promedio de los impares es: ', pi)
print('Los numeros que son menores que 10 son: ', menores)
print('Los números que están entre 20 y 50: ', entre)
print('Los números que son mayores que 100 son: ', mayores)


