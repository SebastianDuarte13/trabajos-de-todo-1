import os
from gestionEquipos import *
from validacion import *
titulo = """
+++++++++++++++++++++++++++++++ 
++++++++++ BET PLAY +++++++++++ 
+++++++++++++++++++++++++++++++ 
"""
def reportes():
  os.system("clear")
  global betplay, titulo
  totalGoles = 0
  bandera = True
  while bandera:
    print(titulo)
    print(
        " A. NOMBRE DEL EQUIPO QUE MAS GOLES ANOTO\n",
         "B. NOMBRE DEL EQUIPO QUE MAS PUNTOS ACUMULO\n",
         "C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO\n",
         "D. TOTAL DE GOLES ANOTADOS POR TODOS LOS EQUIPOS\n",
         "E. PROMEDIO DE GOLES ANOTADOS EN EL TORNEO\n",
         "F. REGRESAR AL MENU ANTERIOR\n",
    )
    selec = input("Bienvenido la sistema de gestion de la liga BetPlay, ingrese la letra de la opcion que desea\n\t").upper()
    if selec == "A":
      masGoles()
      bandera=True
    elif selec == "B":
      masPuntos()
      bandera=True
    elif selec == "C":
      masGano()
      bandera=True
    elif selec == "D":
      totalGoless()
      bandera=True
    elif selec == "E":
      promedio()
      bandera=True
    elif selec == "F":
      bandera = False
    else:
      print("Opcion no valida")

