import art
import os

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificacion(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif 18.5 <= imc < 25:
        return 'Normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    elif 30 <= imc < 35:
        return 'Obeso'
    elif 35 <= imc < 40:
        return 'Obesidad 2'
    elif imc >= 40:
        return 'Obesidad 3'

art.tprint('Bienvenido al centro de salud de Campuslands')
nombre = input("Ingresa tu nombre completo: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kg: "))
os.system('cls')
titulo = """
+++++++++++++++
+   REPORTE   +
+++++++++++++++
"""
print(titulo)
imc = calcular_imc(peso, altura)
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"IMC: {imc}")
print(f"Categoría IMC: {clasificacion(imc)}")



