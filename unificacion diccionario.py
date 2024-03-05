from __future__ import annotations
import os
import art

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = {
            'PJ': 0,
            'PG': 0,
            'PP': 0,
            'PE': 0,
            'GF': 0,
            'GC': 0,
            'TP': 0
        }

equipos = {}

def registrar_equipo():
    os.system('cls')
    cant = int(input("Cuantos equipos deseas agregar? "))
    for i in range(cant):
        nombre = input("Ingrese el nombre del equipo "+ str(i + 1)+': ' )
        equipos[nombre] = Equipo(nombre)
        print(f"Equipo {nombre} registrado correctamente.")
        os.system('pause')
        os.system('cls')

class Partido:
    def __init__(self, equipo_local, equipo_visitante, goles_local, goles_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

def registrar_resultado():
    os.system('cls')
    equipo_local = input("Ingrese el nombre del equipo local: ")
    equipo_visitante = input("Ingrese el nombre del equipo visitante: ")
    goles_local = int(input("Ingrese los goles del equipo local: "))
    goles_visitante = int(input("Ingrese los goles del equipo visitante: "))

    partido = Partido(equipo_local, equipo_visitante, goles_local, goles_visitante)
    actualizar_tabla(partido)
    os.system('cls')

def actualizar_tabla(partido):
    # Actualizar datos de los equipos
    equipo_local = equipos[partido.equipo_local]
    equipo_visitante = equipos[partido.equipo_visitante]

    if partido.goles_local > partido.goles_visitante:
        equipo_local.datos['PG'] += 1
        equipo_visitante.datos['PP'] += 1
    elif partido.goles_local < partido.goles_visitante:
        equipo_visitante.datos['PG'] += 1
        equipo_local.datos['PP'] += 1
    else:
        equipo_local.datos['PE'] += 1
        equipo_visitante.datos['PE'] += 1

    equipo_local.datos['GF'] += partido.goles_local
    equipo_local.datos['GC'] += partido.goles_visitante
    equipo_local.datos['PJ'] += 1

    equipo_visitante.datos['GF'] += partido.goles_visitante
    equipo_visitante.datos['GC'] += partido.goles_local
    equipo_visitante.datos['PJ'] += 1

def reporte_mas_goles_anotados():
    max_goles_equipo = max(equipos.values(), key=lambda equipo: equipo.datos['GF'])
    print(f"El equipo que más goles anotó es: {max_goles_equipo.nombre} con {max_goles_equipo.datos['GF']} goles.")

def reporte_mas_puntos():
    max_puntos_equipo = max(equipos.values(), key=lambda equipo: equipo.datos['TP'])
    print(f"El equipo que más puntos tiene es: {max_puntos_equipo.nombre} con {max_puntos_equipo.datos['TP']} puntos.")

def reporte_mas_partidos_ganados():
    max_partidos_ganados_equipo = max(equipos.values(), key=lambda equipo: equipo.datos['PG'])
    print(f"El equipo que más partidos ganó es: {max_partidos_ganados_equipo.nombre} con {max_partidos_ganados_equipo.datos['PG']} partidos ganados.")

def reporte_total_goles():
    total_goles = sum(equipo.datos['GF'] for equipo in equipos.values())
    print(f"El total de goles anotados por todos los equipos es: {total_goles} goles.")

def reporte_promedio_goles():
    total_equipos = len(equipos)
    total_goles = sum(equipo.datos['GF'] for equipo in equipos.values())
    promedio_goles = total_goles / total_equipos
    print(f"El promedio de goles anotados en el torneo es: {promedio_goles} goles por equipo.")

def generar_reportes():
    os.system('cls')
    reporte_mas_goles_anotados()
    reporte_mas_puntos()
    reporte_mas_partidos_ganados()
    reporte_total_goles()
    reporte_promedio_goles()

def main():
    while True:
        art.tprint ('bienvenidos a la liga betplay')
        titulo="""
        ++++++++++++++++++++++
        +   MENU PRINCIPAL   +
        ++++++++++++++++++++++
        """
        print(titulo)
        diccionario = {1: 'Agregar equipo', 2: 'Agregar fecha', 3: 'Reportes', 4: 'Salir'}

        for key in diccionario:
         print(key, diccionario[key])

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            registrar_resultado()
        elif opcion == "3":
            generar_reportes()
            os.system('pause')
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
