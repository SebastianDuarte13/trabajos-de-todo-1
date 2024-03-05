import os
from validacion import *
betplay = [['NACIONAL', ['PJ',0],['PG',0], ['PP',0], ['PE',0], ['GF',0],['GC',0],['TP',0]],['MEDELLIN', ['PJ',0],['PG',0], ['PP',0], ['PE',0], ['GF',0],['GC',0],['TP',0]]]
fechas = []
titulo = """
+++++++++++++++++++++++++++++++ 
++++++++++ BET PLAY +++++++++++ 
+++++++++++++++++++++++++++++++ 
"""
def registrarEquipo():
    global titulo, betplay
    bandera1=True
    while bandera1:
        os.system("clear")
        print(f"{titulo}")
        print("+++++++ AÑADIR EQUIPOS  +++++++\n")
        nombre = str(input(" Ingrese el nombre del equipo\n\t")).upper()
        equipo = [nombre, ['PJ',0],['PG',0], ['PP',0], ['PE',0], ['GF',0],['GC',0],['TP',0]]
        betplay.append(equipo)
        bandera1=bool(input('¿Desea agregar otro equipo? s(si) ener(no)'))

def gestionFechas():
    bandera2=True
    while bandera2:
        global fechas, betplay, titulo

        os.system("clear")
        print(f"{titulo}\n","++++++ GESTION DE FECHAS ++++++")
        fecha = str(input("Ingrese la fecha de la jornada\n\t"))
        for i in range(len(betplay)):
            print(f"{i+1}. {betplay[i][0]}")
        equipoLocal = int(input("Ingrese el numero del equipo Local\n\t"))
        equipoVisitante = int(input("Ingrese el numero del equipo visitante\n\t"))
        print(f"{betplay[equipoLocal-1][0]} vs {betplay[equipoVisitante-1][0]}")
        golesLocal = int(input("Ingrese los goles del equipo Local\n\t"))
        golesVisitante = int(input("Ingrese los goles del equipo Visitante\n\t"))
        cfecha = [fecha, [betplay[equipoLocal - 1][0], [golesLocal]],
                        [betplay[equipoVisitante - 1][0], [golesVisitante]]]
        fechas.append(cfecha)
        betplay[equipoLocal - 1][1][1] += 1
        betplay[equipoVisitante - 1][1][1] += 1
        betplay[equipoLocal - 1][5][1] += golesVisitante
        betplay[equipoLocal - 1][6][1] += golesLocal
        betplay[equipoVisitante - 1][5][1] += golesVisitante
        betplay[equipoVisitante - 1][6][1] += golesLocal
        if golesLocal > golesVisitante:
            betplay[equipoLocal - 1][2][1] += 1
            betplay[equipoVisitante - 1][3][1] += 1
            betplay[equipoLocal - 1][7][1] += 3
        elif golesLocal < golesVisitante:
            betplay[equipoLocal - 1][2][1] += 1
            betplay[equipoVisitante - 1][3][1] += 1
            betplay[equipoVisitante - 1][7][1] += 3
        else:
            betplay[equipoLocal - 1][4][1] += 1
            betplay[equipoVisitante - 1][4][1] += 1
            betplay[equipoLocal - 1][7][1] += 1
            betplay[equipoVisitante - 1][7][1] += 1

        bandera2=bool(input('¿Desea definir otra fecha? s(si) enter(no)'))

def masGoles():
    mayGoleador=0
    nombre=''
    for i in range(len(betplay)):
        if betplay[i][5][1]>mayGoleador:
            mayGoleador=betplay[i][5][1]
            nombre=betplay[i][0]
    print(f'El equipo goleador de la liga es {nombre}, con {mayGoleador} goles')

def masPuntos():
    mayPuntos=0
    nombre=''
    for i in range(len(betplay)):
        if betplay[i][7][1]>mayPuntos:
            mayPuntos=betplay[i][7][1]
            nombre=betplay[i][0]
    print(f'El equipo ganador de la liga es {nombre}, con {mayPuntos} puntos')

def masGano():
    masJuegosGano=0
    nombre=''
    for i in range(len(betplay)):
        if betplay[i][2][1]>masJuegosGano:
            masJuegosGano=betplay[i][2][1]
            nombre=betplay[i][0]
    print(f'El equipo que mas partidos gano fue {nombre} con un total de {masJuegosGano} partidos ganados')

def totalGoless():
    totalGolesLiga=0
    for i in range(len(betplay)):
        totalGolesLiga += betplay[i][5][1]
    print(f'El total de goles en la liga fue de {totalGolesLiga}')

def promedio():
    totalGolesLiga=0
    for i in range(len(betplay)):
        totalGolesLiga += betplay[i][5][1]
    cantidad= len(fechas)
    prom=totalGolesLiga/cantidad
    print(f'El promedio de goles en la liga fue de {prom} goles por partido')

# def promedio():
    
#     print('PROMEDIOS DE GOLES\n',
#             '1. PROMEDIO DE GOLES POR EQUIPO\n',
#             '2. PROMEDIO DE GOLES EN TORNEO\n',
#             '3. REGRESAR AL MENU ANTERIOR\n',
#             'INGRESE LA OPCION QUE DESEA')
#     opc=valiInt()
#     band=True
#     while band:

#         if opc==1:
#             for i in range(len(betplay)):
#                 print(f"{i+1}. {betplay[i][0]}")
#             elegido=int(input('Ingrese el numero del equipo'))

#             band=True
#         elif opc==2:
            
#             band=True
#         elif opc==3:
#             band=False
#         else:
#             print('Opcion invalida')
#             band=True
    
    

