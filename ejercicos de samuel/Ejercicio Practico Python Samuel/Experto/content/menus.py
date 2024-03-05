import os
import main as m
import funciones.rutas as r
import funciones.campers as c
import funciones.entrenadores as e

menuP = ["Registrar Camper", "Registrar Prueba", "Registro Áreas de Entrenamiento", "Registro Entrenadores", "Creación Rutas de Entrenamiento", "Gestor de Matriculas", "Modulo de Reportes", "Salir"]
menuReporte = ["Campers Inscritos", "Campers Aprobados", "Entrenadores de Campus", "Campers con bajo rendimiento", "Buscar Ruta de Entrenamiento", "Resumen de Módulos", "Volver"]

import os
import main as main_module
import funciones.rutas as routes
import funciones.campers as campers
import funciones.entrenadores as trainers

menu_principal = ["Registrar Camper", "Registrar Prueba", "Registro Áreas de Entrenamiento", "Registro Entrenadores", "Creación Rutas de Entrenamiento", "Gestor de Matrículas", "Módulo de Reportes", "Salir"]
menu_reporte = ["Campers Inscritos", "Campers Aprobados", "Entrenadores de Campus", "Campers con bajo rendimiento", "Buscar Ruta de Entrenamiento", "Resumen de Módulos", "Volver"]

def mostrar_menu_principal():
    campers.cf.checkFile(main_module.campus)
    header = """
    *************************************
    * SEGUIMIENTO ACADÉMICO CAMPUSLANDS *
    *************************************
    """
    print(header)
    for i, item in enumerate(menu_principal):
        print(f"{i+1} - {item}")

def mostrar_menu_reporte():
    header = """
    *************************************
    *        MÓDULO DE REPORTES         *
    *************************************
    """

    is_incorrecto = True
    op_menu = 0
    while is_incorrecto:
        os.system("cls")
        print(header)
        for i, item in enumerate(menu_reporte):
            print(f"{i+1} - {item}")
        try:
            op_menu = int(input("Ingrese una opción : "))
        except ValueError:
            print("Tipo de dato incorrecto")
        else:
            if op_menu == 1:
                os.system("cls")
                campers.campersInscritos(main_module.campus)
            elif op_menu == 2:
                os.system("cls")
                campers.campersAprobados(main_module.campus)
            elif op_menu == 3:
                os.system("cls")
                trainers.entrenadoresCampus(main_module.campus)
            elif op_menu == 4:
                os.system("cls")
                campers.campersBajoRendimiento(main_module.campus)
            elif op_menu == 5:
                os.system("cls")
                id_ruta = routes.buscarRuta(main_module.campus)
                routes.mostrarRuta(id_ruta, main_module.campus)
            elif op_menu == 6:
                os.system("cls")
            elif op_menu == 7:
                is_incorrecto = False
