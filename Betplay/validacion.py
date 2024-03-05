
def valiInt():
    bandera=True
    while bandera:
        try:
            x =int(input())
            return x
        except:
            print('Solo se aceptan numero enteros, digite nuevamente')
            return valiInt
    
def valiStr():
    bandera=True
    while bandera:
        try:
            x =str(input())
            return x
        except:
            print('Solo se aceptan numero enteros, digite nuevamente')
            return valiStr()