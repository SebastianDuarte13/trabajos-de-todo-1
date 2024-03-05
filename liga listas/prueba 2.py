class Partido:
    def __init__(self, equipo_local, equipo_visitante, goles_local, goles_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

def registrar_resultado():
    equipo_local = input("Ingrese el nombre del equipo local: ")
    equipo_visitante = input("Ingrese el nombre del equipo visitante: ")
    goles_local = int(input("Ingrese los goles del equipo local: "))
    goles_visitante = int(input("Ingrese los goles del equipo visitante: "))

    partido = Partido(equipo_local, equipo_visitante, goles_local, goles_visitante)
    actualizar_tabla(partido)

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

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar equipo")
        print("2. Registrar resultado de un partido")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            registrar_resultado()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
