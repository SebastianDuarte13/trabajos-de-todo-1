from torneo import *

def main():
    torneo = Torneo()

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
    categoria = input("Ingrese la categoría del jugador (Novato/Intermedio/Avanzado): ")
    id_jugador = input("Ingrese el ID del jugador: ")
    nombre = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador: "))
    torneo.registrar_jugador(categoria, id_jugador, nombre, edad)
    print("Jugador registrado con éxito.")

def mostrar_ganadores(torneo):
    for categoria in torneo.categorias:
        ganador = torneo.obtener_ganador_categoria(categoria)
        if ganador:
            print(f"Ganador en la categoría {categoria}: {ganador.nombre}")
        else:
            print(f"No hay jugadores registrados en la categoría {categoria}.")

if __name__ == "__main__":
   pass
