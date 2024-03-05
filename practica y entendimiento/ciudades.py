import os
def registro(ciudades):
    nombre = input("Ingrese el nombre de la ciudad: ")
    ciudades.append({"nombre": nombre, "sismos": []})
    print("Ciudad registrada correctamente.")
    os. system('pause')

def buscar(ciudades, nombre):
    for ciudad in ciudades:
        if ciudad["nombre"] == nombre:
            return ciudad
    return None
