class Dependencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.consumo_electricidad = 0
        self.kilometros_recorridos = 0
        self.factor_emision_electricidad = 0
        self.factor_emision_transporte = 0

    def registrar_consumo_electricidad(self, consumo, factor_emision):
        self.consumo_electricidad += consumo
        self.factor_emision_electricidad = factor_emision

    def registrar_consumo_transporte(self, kilometros, factor_emision):
        self.kilometros_recorridos += kilometros
        self.factor_emision_transporte = factor_emision

    def calcular_emision_co2(self):
        emision_electricidad = self.consumo_electricidad * self.factor_emision_electricidad
        emision_transporte = self.kilometros_recorridos * self.factor_emision_transporte
        return emision_electricidad + emision_transporte


dependencias = []

def registrar_dependencia():
    nombre = input("Ingrese el nombre de la dependencia: ")
    dependencia = Dependencia(nombre)
    dependencias.append(dependencia)
    print("Dependencia registrada con éxito.")

def registrar_consumo():
    nombre = input("Ingrese el nombre de la dependencia: ")
    for dependencia in dependencias:
        if dependencia.nombre == nombre:
            consumo_electricidad = float(input("Ingrese el consumo de electricidad en kWh: "))
            factor_emision_electricidad = float(input("Ingrese el factor de emisión de electricidad: "))
            dependencia.registrar_consumo_electricidad(consumo_electricidad, factor_emision_electricidad)

            kilometros_recorridos = float(input("Ingrese los kilómetros recorridos en transporte: "))
            factor_emision_transporte = float(input("Ingrese el factor de emisión del transporte: "))
            dependencia.registrar_consumo_transporte(kilometros_recorridos, factor_emision_transporte)

            print("Consumo registrado con éxito.")
            return
    print("No se encontró la dependencia.")

def ver_co2_producido():
    for dependencia in dependencias:
        emision_co2 = dependencia.calcular_emision_co2()
        print(f"Dependencia: {dependencia.nombre}, Emisión CO2: {emision_co2} tCO2eq")

def dependencia_mayor_co2():
    if not dependencias:
        print("No hay dependencias registradas.")
        return

    max_emision_co2 = -1
    dependencia_max_co2 = None
    for dependencia in dependencias:
        emision_co2 = dependencia.calcular_emision_co2()
        if emision_co2 > max_emision_co2:
            max_emision_co2 = emision_co2
            dependencia_max_co2 = dependencia

    print(f"La dependencia que produce mayor CO2 es: {dependencia_max_co2.nombre}")

while True:
    print("\nMenú Principal:")
    print("1. Registrar Dependencia")
    print("2. Registrar consumo por dependencia")
    print("3. Ver CO2 producido")
    print("4. Dependencia que produce mayor CO2")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_dependencia()
    elif opcion == '2':
        registrar_consumo()
    elif opcion == '3':
        ver_co2_producido()
    elif opcion == '4':
        dependencia_mayor_co2()
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

