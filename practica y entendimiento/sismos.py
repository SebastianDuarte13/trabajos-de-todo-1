def registrar_sismo(ciudad):
    magnitud = float(input("Ingrese la magnitud del sismo: "))
    ciudad["sismos"].append(magnitud)
    print("Sismo registrado correctamente.")

def calcular_promedio_sismos(ciudad):
    return sum(ciudad["sismos"]) / len(ciudad["sismos"])

def generar_informe_riesgo(promedio_sismos):
    if promedio_sismos < 2.5:
        return "Amarillo (Sin riesgo)"
    elif 2.5 <= promedio_sismos <= 4.5:
        return "Naranja (Riesgo medio)"
    else:
        return "Rojo (Riesgo alto)"

