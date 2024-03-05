
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
    nombre = input("Ingrese el nombre del equipo: ")
    equipo = Equipo(nombre)
    equipos.append(equipo)
    print(f"Equipo {nombre} registrado correctamente.")

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar equipo")
        print("2. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
