import modulos.corefile as file_functions

def verificar_nota(valor_dato, enunciado_dato, tipo_dato) -> int:
    global is_incorrect
    is_incorrect = True
    valor_dato = 0
    while is_incorrect:
        try:
            valor_dato = tipo_dato(input(f"{enunciado_dato}"))
        except ValueError:
            print(f"Tipo de dato incorrecto")
        else:
            if int(valor_dato) >= 0 and int(valor_dato) <= 100:
                is_incorrect = False
            elif tipo_dato == str and valor_dato == "":
                print(f"El dato no debe estar vacío")
            else:
                print(f"Ingrese un valor entre 0 y 100")
    return valor_dato

def registrar_prueba(id_camper: str, campus: dict):
    data = campus.get("campus").get("campers").get(id_camper, -1)
    
    if type(data) == dict:
        valor = 0
        if data["Estado"] == "Inscrito":
            nota_teorica = verificar_nota(valor, "Ingrese el valor de la nota teórica (0 a 100): ", int)
            nota_practica = verificar_nota(valor, "Ingrese el valor de la nota práctica (0 a 100): ", int)
            nota_total = (nota_teorica + nota_practica) / 2
            if nota_total >= 60:
                estado = "Aprobado"
            else:
                estado = "Desaprobado"
            prueba = {
                "id_camper": id_camper,
                "nota": nota_total,
                "estado": estado
            }
            data_pruebas = campus.get("campus").get("pruebas")
            data_pruebas.update({str((len(data_pruebas) + 1)).zfill(3): prueba})
            campus.get("campus").get("pruebas").update(data_pruebas)
            data.update({"Estado": estado})
            file_functions.UpdateFile(campus)
        elif data["Estado"] == "Matriculado":
            id_modulo = ""
            while id_modulo not in ["1", "2", "3", "4", "5"]:
                id_modulo = verificar_nota(valor, "Ingrese el id del módulo cuyas pruebas quiere registrar: ", str)
            
            nota_teorica = verificar_nota(valor, "Ingrese el valor de la nota teórica (0 a 100): ", int)
            nota_practica = verificar_nota(valor, "Ingrese el valor de la nota práctica (0 a 100): ", int)
            nota_quices_trabajos = verificar_nota(valor, "Ingrese el valor de la nota de quices y trabajos (0 a 100): ", int)
            nota_total = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_quices_trabajos * 0.1)
            if nota_total >= 60:
                estado = "Matriculado"
            else:
                estado = "En Riesgo"
            prueba = {
                "id_camper": id_camper,
                "id_modulo": id_modulo,
                "nota": nota_total,
                "estado": estado
            }
            data_pruebas = campus.get("campus").get("pruebas")
            data_pruebas.update({str((len(data_pruebas) + 1)).zfill(3): prueba})
            campus.get("campus").get("pruebas").update(data_pruebas)
            data.update({"Estado": estado})
            file_functions.UpdateFile(campus)
        else:
            print(f"El estado del Camper no es Matriculado")
    else:
        print(f"No se encontró el id")