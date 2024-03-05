def registrar_area_entrenamiento():
    titulo="""
    +++++++++++++++++++++++++++
    +   LUGARES CAMPUSLANDS   +
    +++++++++++++++++++++++++++
    """
    print(titulo)
    
    areas = []
    num_areas = int(input("¿Cuántas áreas de entrenamiento desea registrar? "))
    
    for i in range(num_areas):
        print(f"\n--- Área de entrenamiento {i+1} ---")
        nombre = input("Ingrese el nombre del área de entrenamiento: ")
        areas.append({'area_entrenamiento': nombre, 'capacidad maxima': '33 campers'})
    
    return areas

print(registrar_area_entrenamiento())
