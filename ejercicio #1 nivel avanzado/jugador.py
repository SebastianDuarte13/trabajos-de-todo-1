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
