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
