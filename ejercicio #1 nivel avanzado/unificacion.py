class Jugador:
    def __init__(self, id_jugador, nombre, edad):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.edad = edad
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_perdidos = 0
        self.puntos_a_favor = 0
        self.total_puntos = 0

    def calcular_puntos_a_favor(self, puntos_realizados, puntos_recibidos):
        self.puntos_a_favor += puntos_realizados - puntos_recibidos

    def registrar_victoria(self):
        self.partidos_ganados += 1
        self.total_puntos += 2

    def registrar_derrota(self):
        self.partidos_perdidos += 1


class TorneoTenisDeMesa:
    def __init__(self):
        self.jugadores = {"Novato": [], "Intermedio": [], "Avanzado": []}

    def registrar_jugador(self, categoria, jugador):
        self.jugadores[categoria].append(jugador)

    def iniciar_juegos(self):
        for categoria, jugadores in self.jugadores.items():
            if len(jugadores) < 5:
                print(f"No hay suficientes jugadores en la categoría {categoria} para iniciar los juegos.")
                continue
            print(f"Iniciando juegos en la categoría {categoria}...")
            # Lógica para llevar a cabo los juegos en la categoría

    def obtener_ganador_categoria(self, categoria):
        jugadores_categoria = self.jugadores[categoria]
        if jugadores_categoria:
            ganador = max(jugadores_categoria, key=lambda jugador: jugador.puntos_a_favor)
            return ganador
        else:
            return None


def main():
    torneo = TorneoTenisDeMesa()

    while True:
        print("\nMenú Principal:")
        print("1. Registrar Jugador")
        print("2. Iniciar Juegos")
        print("3. Mostrar Ganadores por Categoría")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_jugador(torneo)
        elif opcion == '2':
            torneo.iniciar_juegos()
        elif opcion == '3':
            mostrar_ganadores(torneo)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def registrar_jugador(torneo):
    categoria = input("Ingrese la categoría del jugador (Novato/Intermedio/Avanzado): ").capitalize()
    if categoria not in ["Novato", "Intermedio", "Avanzado"]:
        print("Categoría no válida.")
        return

    id_jugador = input("Ingrese el ID del jugador: ")
    nombre = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador: "))

    if (categoria == "Novato" and 15 <= edad <= 16) or \
            (categoria == "Intermedio" and 17 <= edad <= 20) or \
            (categoria == "Avanzado" and edad > 20):
        jugador = Jugador(id_jugador, nombre, edad)
        torneo.registrar_jugador(categoria, jugador)
        print("Jugador registrado con éxito.")
    else:
        print("La edad del jugador no es válida para la categoría seleccionada.")


def mostrar_ganadores(torneo):
    for categoria in torneo.jugadores:
        ganador = torneo.obtener_ganador_categoria(categoria)
        if ganador:
            print(f"Ganador en la categoría {categoria}: {ganador.nombre}")
        else:
            print(f"No hay jugadores registrados en la categoría {categoria}.")


if __name__ == "__main__":
    main()
