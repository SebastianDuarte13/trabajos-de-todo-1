from jugador import Jugador

class Torneo:
    def __init__(self):
        self.categorias = {"Novato": [], "Intermedio": [], "Avanzado": []}

    def registrar_jugador(self, categoria, id_jugador, nombre, edad):
        jugador = Jugador(id_jugador, nombre, edad)
        self.categorias[categoria].append(jugador)

    def iniciar_juegos(self):
        for categoria, jugadores in self.categorias.items():
            if len(jugadores) >= 5:
                print(f"Iniciando juegos en la categoría {categoria}")
                # Lógica para llevar a cabo los juegos en la categoría
            else:
                print(f"No hay suficientes jugadores en la categoría {categoria} para iniciar los juegos.")

    def obtener_ganador_categoria(self, categoria):
        jugadores_categoria = self.categorias[categoria]
        if jugadores_categoria:
            ganador = max(jugadores_categoria, key=lambda jugador: jugador.puntos_a_favor)
            return ganador
        else:
            return None
