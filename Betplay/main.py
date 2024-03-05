import os
from menuReportes import *
from validacion import *


titulo = """
+++++++++++++++++++++++++++++++ 
++++++++++ BET PLAY +++++++++++ 
+++++++++++++++++++++++++++++++ 
"""

bandera = True
while bandera:
    os.system('cls')
    print(titulo)
    print(" 1. AÑADIR EQUIPOS\n",
           "2. GESTION DE FECHAS\n", 
           "3. REPORTES\n",
           "4. SALIR")
    print("Bienvenido la sistema de gestion de lanliga BetPlay, ingrese el numero de la opcion que desea\n\t")
    opc = valiInt()
    if opc == 1:
        registrarEquipo()
        bandera=True
    elif opc == 2:
        gestionFechas()
        bandera=True
    elif opc == 3:
        reportes()
        bandera=True
    elif opc == 4:
        os.system("clear")
        print('Vuelva pronto')
        bandera = False
    else:
        print("Opcion no valida")
        bandera=True
