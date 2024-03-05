from registro_camper import id_del_camper

def registrar_prueba():
    id_camper = input("Ingrese el ID del camper: ")
    
    if id_camper not in id_del_camper:
        print("El ID del camper no está registrado.")
        return
    
    nota_teorica = float(input("Ingrese la nota teórica (0-100): "))
    nota_practica = float(input("Ingrese la nota práctica (0-100): "))
    promedio = (nota_teorica + nota_practica) / 2

    if promedio >= 60:
        id_del_camper[id_camper]['Estado'] = 'Aprobado'
    else:
        id_del_camper[id_camper]['Estado'] = 'Reprobado'

    id_del_camper[id_camper]['Nota Teórica'] = nota_teorica
    id_del_camper[id_camper]['Nota Práctica'] = nota_practica
    id_del_camper[id_camper]['Promedio'] = promedio


print(({}))

# Llamada a la función e impresión del resultado






#print(reg_prueba({}))