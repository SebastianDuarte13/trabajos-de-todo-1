i=5
ciudades=[]
def registro_ciudades():
    while i>=0:
        k=input("Ingrese el nombre de la ciudad")
        ciudades.append(k)
        i-=1
    print(ciudades)