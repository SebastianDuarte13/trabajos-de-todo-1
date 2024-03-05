#Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
#Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.
#Total de números ingresados
#Total de números pares ingresados
#Promedio de los números pares
#Promedio de los números impares
#números son menores que 10
#números están entre 20 y 50
#números son mayores que 100
import os, art

numerostotales = 0
totalpares = 0
sumapares = 0
totalimpares = 0
sumaimpares = 0
menoresde10 = 0
entre20y50 = 0
masde100 = 0

art.tprint("Calculadora de Positivos")
while True:
    numero = int(input("Ingresa un numero positivo (O un negativo para parar): "))
    if numero < 0:
        break
    numerostotales += 1

    if numero % 2 == 0:
        totalpares += 1
        sumapares += numero
    else:
        totalimpares += 1
        sumaimpares += numero

    if numero < 10:
        menoresde10 += 1
    if 20 <= numero <= 50:
        entre20y50 += 1
    if numero > 100:
        masde100 += 1

promedio_pares = sumapares / totalpares if totalpares > 0 else 0
promedio_impares = sumaimpares / totalimpares if totalimpares > 0 else 0
os.system("cls")

art.tprint("\nRsultados:")
print("\ta. Total de numeros ingresados:", numerostotales)
print("\tb. Total de numeros pares ingresados:", totalpares)
print("\tc. Promedio de los numeros pares:", promedio_pares)
print("\td. Promedio de los numeros impares:", promedio_impares)
print("\te. Numeros menores que 10:", menoresde10)
print("\tf. Numeros entre 20 y 50:", entre20y50)
print("\tg. Numeros mayores de 100:", masde100)