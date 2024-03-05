import os
bandera = True
def menureportes():
    titulo="""
    ++++++++++++++++++++++++++++++++++
    + BIENVENIDO AL MENU DE REPORTES +
    ++++++++++++++++++++++++++++++++++
    """
    print(titulo)
  while bandera:
        menureportes = {'A': 'Equipo con más goles', 'B': 'Equipo con más partidos ganados', 'C': 'Equipo con más puntos', 'D': 'Total de goles del torneo', 'E': 'Promedio de goles ', 'F':'Volver al menu principal'}
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