import os

def calcular_nota_final(nota_practica, nota_teorica):
    
    nota_final = nota_practica * 0.85 + nota_teorica * 0.15
    return nota_final

def evaluar_estudiantes(num_estudiantes):
    
    mejor_estudiante = ("", float("-inf"))  
    peor_estudiante = ("", float("inf"))   

    for _ in range(num_estudiantes):
        os.system('cls')
        nombre = input("Ingrese el nombre del estudiante: ")
        
        nota_practica = None
        while nota_practica is None:
            try:
                nota_practica = float(input("Ingrese la nota del examen práctico : "))
                if nota_practica < 0 or nota_practica > 100:
                    raise ValueError("La nota debe estar en el rango de 0 a 100.")
            except ValueError as e:
                print(e)
                nota_practica = None
        
        nota_teorica = None
        while nota_teorica is None:
            try:
                nota_teorica = float(input("Ingrese la nota del examen teórico : "))
                if nota_teorica < 0 or nota_teorica > 100:
                    raise ValueError("La nota debe estar en el rango de 0 a 100.")
            except ValueError as e:
                print(e)
                nota_teorica = None

        nota_final = calcular_nota_final(nota_practica, nota_teorica)

        print(f"La nota final de {nombre} es: {nota_final}")

        if nota_final > mejor_estudiante[1]:
            mejor_estudiante = (nombre, nota_final)

        if nota_final < peor_estudiante[1]:
            peor_estudiante = (nombre, nota_final)

    return mejor_estudiante, peor_estudiante

if __name__ == "__main__":
    num_estudiantes = int(input("Ingrese el número de estudiantes: "))
    mejor_estudiante, peor_estudiante = evaluar_estudiantes(num_estudiantes)

    os.system('cls')
    print(f"\nEl estudiante con la mayor nota es: {mejor_estudiante[0]} con una nota de {mejor_estudiante[1]}")
    print(f"El estudiante con la menor nota es: {peor_estudiante[0]} con una nota de {peor_estudiante[1]}")
