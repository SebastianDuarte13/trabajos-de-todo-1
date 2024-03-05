from __future__ import annotations
import os
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.PJ = 0
        self.PG = 0
        self.PP = 0
        self.PE = 0
        self.GF = 0
        self.GC = 0
        self.TP = 0

equipos = []

def registrar_equipo():
    os.system('cls')
    nombre = input("Ingrese el nombre del equipo: ")
    equipo = Equipo(nombre)
    equipos.append(equipo)
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
    equipo_local = next((equipo for equipo in equipos if equipo.nombre == partido.equipo_local), None)
    equipo_visitante = next((equipo for equipo in equipos if equipo.nombre == partido.equipo_visitante), None)

    if partido.goles_local > partido.goles_visitante:
        equipo_local.PG += 1
        equipo_visitante.PP += 1
    elif partido.goles_local < partido.goles_visitante:
        equipo_visitante.PG += 1
        equipo_local.PP += 1
    else:
        equipo_local.PE += 1
        equipo_visitante.PE += 1

    equipo_local.GF += partido.goles_local
    equipo_local.GC += partido.goles_visitante
    equipo_local.PJ += 1

    equipo_visitante.GF += partido.goles_visitante
    equipo_visitante.GC += partido.goles_local
    equipo_visitante.PJ += 1

def reporte_mas_goles_anotados():
    max_goles_equipo = max(equipos, key=lambda equipo: equipo.GF)
    print(f"El equipo que más goles anotó es: {max_goles_equipo.nombre} con {max_goles_equipo.GF} goles.")

def reporte_mas_puntos():
    max_puntos_equipo = max(equipos, key=lambda equipo: equipo.TP)
    print(f"El equipo que más puntos tiene es: {max_puntos_equipo.nombre} con {max_puntos_equipo.TP} puntos.")

def reporte_mas_partidos_ganados():
    max_partidos_ganados_equipo = max(equipos, key=lambda equipo: equipo.PG)
    print(f"El equipo que más partidos ganó es: {max_partidos_ganados_equipo.nombre} con {max_partidos_ganados_equipo.PG} partidos ganados.")

def reporte_total_goles():
    total_goles = sum(equipo.GF for equipo in equipos)
    print(f"El total de goles anotados por todos los equipos es: {total_goles} goles.")

def reporte_promedio_goles():
    total_equipos = len(equipos)
    total_goles = sum(equipo.GF for equipo in equipos)
    promedio_goles = total_goles / total_equipos
    print(f"El promedio de goles anotados en el torneo es: {promedio_goles} goles por equipo.")

def generar_reportes():
    reporte_mas_goles_anotados()
    reporte_mas_puntos()
    reporte_mas_partidos_ganados()
    reporte_total_goles()
    reporte_promedio_goles()

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar equipo")
        print("2. Registrar resultado de un partido")
        print("3. Generar reportes")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            registrar_resultado()
        elif opcion == "3":
            generar_reportes()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
