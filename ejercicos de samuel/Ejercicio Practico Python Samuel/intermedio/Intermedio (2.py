#la alcaldia de bucaramanga desea realizar un programa que le permita calcular el valor de CO2 producido en las diferentes instalaciones gubernamentales de la ciudad

#tenga en cuenta las siguientes observaciones:

#transporte
#incluye las emisiones asociadas con el transporte, ya sea propio o mediante servicios de transporte publico
#emisiones de CO2(transporte) = kilometros recorridos * factor de emision del transporte

#consumo de electricidad
#consumo de electricidad: obten tus facturas de electricidad y veridica el consumo mensual o anuel en kilovatios-hora (kWh)
#utiliza el factor de emision de tu region para convertir el consumo de electricidad a emisiones de CO2
#este factor puede variar segun la fuente de generacion de electricidad en tu area
#emisiones de CO2 (electricidad) = Consumo de electricidad * factor de emision de electricidad

#para calcular el consumo de electricidad, sigue los siguientes pasos:

#obten tu factura de electricidad:
#la factura de electricidad proporciona ingormacion detallada sobre tu consumo, busca el total de kilovatios-hora (kWh) utilizado durante el periodo facturado
#identifica el periodo de facturacion:
#asegurate de conocer el periodo de tiempo al que se refiere la factura, ya que los cargos pueden ser mensuales, bimestrales o segun otro intervalo.

#calculo del consumo mensual o anual:
#si la factura muestra el consumo mensual, no necesitas hacer mas calculos. sin embargo, si se proporciona el consumo bimestral o en un intervalo diferente,
#puedes dividir ese valor por el numero de meses en ese periodo para obtener un promedio mensual.
#consumo mensual = consumo bimestral/numero de meses en el periodo

#si se busca un desglose mas detallado, algunos electrodomesticos o dispositivos proporcionan ingormacion especifica sobre su consumo de energia en watts (w)
#la persona puede utilizar esta informacion para calcular el consumo de estos dispositivos en kilovatios-hora (kWh)

#consumo de dispositivo = potencia del dispositivo en W * Tiempo de uso en horas / 1000

#despues se puede realizar la suma de los consumosss individuales para obtener el total.

#la energia hidraulica, que es la fuente de energia mas limpia tiene un factor de emision de 0 tCO2uq/MWh. la energia termina, que incluye la generacion de energia a partir de
#combustibles fosiles como el carbom, el petroleo y el gas natural, tiene un factor de emision de entre 0.3 y 0.7 tCO2eq/MWh. la energia renovable no convencional, que incluye
#la generacion de energia a partir de fuentes como la solar, la eolica y la geotermica, tiene un factor de emision de entre 0 y 0,1 tCO2eq/MWh.

#el programa debe permitir mostrar cual de las instalaciones tiene mayor produccion de CO2
#REQUERIMIENTOS: El programa debe contar con un menu principal que permita realizar todos los procesos solicitados.

#1) registrar dependencia
#2) registrar consumo por dependencia: tener en cuenta que se debe registrar los valores consumidos por los dispositivos en cada una de las oficinas.
#3) ver CO2 producido
#4) dependencia que produce mayor CO2
#5) Salir
import os, art

def menu():
    art.tprint("Menu")
    print("1. Registrar dependencia")
    print("2. Registrar consumo por dependencia")
    print("3. Ver CO2 producido")
    print("4. Dependencia con mayor produccion")
    print("5. Salir")

def registrar_dependencia():
    os.system("cls")
    art.tprint("Registrar Dependencia")

def registrar_consumo():
    os.system("cls")
    art.tprint("Registrar Consumo")

def ver_produccion():
    os.system("cls")
    art.tprint("Produccion")

def dependencia_mayor():
    os.system("cls")
    art.tprint("Dependencia Mayor")

while True:
    menu()
    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        registrar_dependencia()
    elif opcion == 2:
        registrar_consumo()
    elif opcion == 3:
        ver_produccion()
    elif opcion == 4:
        dependencia_mayor()
    elif opcion == 5:
        break
    else:
        print("Opción no válida")