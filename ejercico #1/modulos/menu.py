model=True
from tabulate import tabulate
import os
from menureportes import*
import art
import pickle
import tabulate
art.tprint('BIENVENIDOS A LA LIGA BETPLAY')

equipos = {}diccionario = {1: 'Agregar equipo', 2: 'Agregar fecha', 3: 'Tabla de posiciones', 4: 'reportes', 5: 'salir'}
liga = {}

def agregar_equipo():
    
    cant = int(input("Cuantos equipos deseas agregar? "))
    for i in range(cant):
        nombre = input("Nombre del equipo " + str(i + 1) + ": ")
        clasi = input(f"Porfavor digite si el equipo es local o visitante ")
        if clasi == 'local':
            if 'local' not in liga:
                liga['local'] = []
            liga['local'].append(nombre)
        elif clasi == 'visitante':
            if 'visitante' not in liga:
                liga['visitante'] = []
            liga['visitante'].append(nombre)
        else:
            print('Opción incorrecta')
            os.system('cls')
        print(f'el primer partido se disputara entre'+nombre(i+1))
        goles= int(input(f'cuantos goles anoto '+nombre+ ':'))
        
    print('Para volver al menu principal ingrese cualquier tecla')
    os.system('pause')
