import art
import os

bp = 0
n = 0
sp = 0
ob1 = 0
ob2 = 0
ob3 = 0

def registro_nombres():
    nombres = []
    for i in range(1, 3):
        nombre = input(f"Ingrese el nombre {i}: ")
        peso = int(input(f"Ingrese el peso de {nombre} en kg: "))
        altura = float(input(f"Ingrese la altura de {nombre} en metros: "))
        imc = peso / (altura ** 2)
        nombres.append((nombre, peso, imc))
        os.system('cls')
    return nombres

def clasificacion(imc):
    global bp, n, sp, ob1, ob2, ob3
    if imc < 18.5:
        print('Bajo de peso')
        bp += 1
    elif 18.5 <= imc < 25:
        print ('Estas normal')
        n += 1
    elif 25 <= imc < 30:
        print ('Tienes Sobrepeso')
        sp += 1
    elif 30 <= imc < 35:
        print ('Tienes Obesidad I')
        ob1 += 1
    elif 35 <= imc < 40:
        print ('Tienes Obesidad II')
        ob2 += 1
    elif imc >= 40:
        print ('Tienes Obesidad III')
        ob3 += 1

def calcular_imc():
    for nombre, peso, imc in nombres:
        print(f"Nombre: {nombre}")
        print(f"IMC: {imc}")
        print(f"clasificado como {clasificacion(imc)}")
        print()

art.tprint('Bienvenido al centro de salud de Campuslands')

nombres = []

while True:
    titulo = """
    ++++++++++++++++++++++
    +   Menu principal   +
    ++++++++++++++++++++++
    """
    print(titulo)
    print("1. Registrar nombres")
    print("2. Datos de los estudiantes")
    print("3. Generar reportes de los estudiantes")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        os.system('cls')
        nombres = registro_nombres()
        print('Registro completado')
        os.system('pause')
    elif opcion == "2":
        os.system('cls')
        titulo = """
        +++++++++++++++++++++++++
        +   Datos estudiantes   +
        +++++++++++++++++++++++++
        """
        print(titulo)
        if nombres:
            calcular_imc()
        os.system('pause')
        os.system('cls')
    elif opcion == "3":
        titulo = """
        ++++++++++++++++++++++++++++
        +   Reportes estudiantes   +
        ++++++++++++++++++++++++++++
        """
        print(titulo)
        print('Número de estudiantes con bajo peso: ', bp)
        print('Número de estudiantes con IMC Normal: ', n)
        print('Número de estudiantes con Sobrepeso: ', sp)
        print('Número de estudiantes con Obesidad I: ', ob1)
        print('Número de estudiantes con Obesidad II: ', ob2)
        print('Número de estudiantes con Obesidad III: ', ob3)
        os.system('pause')
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")




    
    

