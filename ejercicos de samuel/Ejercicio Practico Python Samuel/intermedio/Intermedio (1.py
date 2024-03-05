#El centro de prevención de sismos en Colombia desea realizar un programa que le permita llevar el
#Registro del los sismos presentados en 5 ciudades del país. Por cada ciudad se realizan n cantidad de
#Registros. El programa debe permitir registrar las muestras del movimiento en cada ciudad.

#Requerimientos:
#El programa debe tener un menú con las siguientes opciones
#Registrar Ciudad
#Registrar Sismo
#Buscar sismos por ciudad
#Informe de riesgo
#Salir

#Restricciones:
#Todas las ciudades deben tener la misma cantidad de sismos registrado
#El informe de riesgos presenta la siguiente clasificación:
#Amarillo (Sin riesgo) : El promedio de los sismos es < 2,5
#Naranja (Riesgo medio) : El promedio de los sismos esta entre 2.6 y 4.5
#Rojo (Riesgo alto) : El promedio de los sismos es mayor a 4.5
#solución debe implementar listas , listas dentro de listas y modulos
import statistics, os, art

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sismos = []

    def agregar_sismo(self, sismo):
        self.sismos.append(sismo)

    def calcular_promedio(self):
        if len(self.sismos) == 0:
            return 0
        return statistics.mean([sismo.magnitud for sismo in self.sismos])

    def informe_riesgo(self):
        promedio = self.calcular_promedio()
        if promedio < 2.5:
            return "Amarillo (Sin riesgo)"
        elif 2.6 <= promedio <= 4.5:
            return "Naranja (Riesgo medio)"
        else:
            return "Rojo (Riesgo alto)"

class Sismo:
    def __init__(self, magnitud, ciudad):
        self.magnitud = magnitud
        self.ciudad = ciudad

def menu():
    art.tprint("Menu")
    print("1. Registrar Ciudad")
    print("2. Registrar Sismo")
    print("3. Buscar sismos por ciudad")
    print("4. Informe de riesgo")
    print("5. Salir")

def registrar_ciudad():
    os.system("cls")
    art.tprint("Registro de ciudad")
    nombre = input("Ingrese el nombre de la ciudad: ")
    ciudad = Ciudad(nombre)
    art.tprint("Ciudad Registrada")
    os.system("pause")
    os.system("cls")
    return ciudad

def registrar_sismo():
    os.system("cls")
    art.tprint("Registro de sismo")
    ciudad = input("Ingrese el nombre de la ciudad: ")
    magnitud = float(input("Ingrese la magnitud del sismo: "))
    ciudad_obj = None
    for ciudad in ciudades:
        if ciudad.nombre == ciudad:
            ciudad_obj = ciudad
            os.system("cls")
            art.tprint("Sismo Registrado")
            os.system("pause")
            os.system("cls")
            break
    if ciudad_obj is None:
        os.system("cls")
        art.tprint("Ciudad no encontrada")
        os.system("pause")
        os.system("cls")
        return
    sismo = Sismo(magnitud, ciudad_obj)
    ciudad_obj.agregar_sismo(sismo)

def buscar_sismos_por_ciudad():
    os.system("cls")
    art.tprint("Busqueda de sismos")
    ciudad = input("Ingrese el nombre de la ciudad: ")
    for ciudad_obj in ciudades:
        if ciudad_obj.nombre == ciudad:
            print("Sismos en {}:".format(ciudad_obj.nombre))
            os.system("pause")
            os.system("cls")
            for sismo in ciudad_obj.sismos:
                print("Magnitud: {}, Ciudad: {}".format(sismo.magnitud, sismo.ciudad.nombre))
                os.system("pause")
                os.system("cls")
            break
    else:
        print("Ciudad no encontrada")
        os.system("pause")
        os.system("cls")
def informe_riesgo():
    os.system("cls")
    art.tprint("Informe de riesgo")
    ciudad = input("Ingrese el nombre de la ciudad: ")
    for ciudad_obj in ciudades:
        if ciudad_obj.nombre == ciudad:
            print("Informe de riesgo para {}: {}".format(ciudad_obj.nombre, ciudad_obj.informe_riesgo()))
            os.system("pause")
            os.system("cls")
            break
    else:
        art.tprint("Ciudad no encontrada")
        os.system("pause")
        os.system("cls")

ciudades = []

while True:
    menu()
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        ciudad = registrar_ciudad()
        ciudades.append(ciudad)
    elif opcion == 2:
        registrar_sismo()
    elif opcion == 3:
        buscar_sismos_por_ciudad()
    elif opcion == 4:
        informe_riesgo()
    elif opcion == 5:
        break
    else:
        print("Opción no válida")