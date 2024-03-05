from producto import Producto
from inventario import Inventario

def main():
    inventario = Inventario()

    while True:
        print("\nMenú Principal:")
        print("1. Registro de Productos")
        print("2. Visualización de Productos")
        print("3. Actualización de Stock")
        print("4. Informe de Productos Críticos")
        print("5. Cálculo de Ganancia Potencial")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_producto(inventario)
        elif opcion == '2':
            inventario.visualizar_productos()
        elif opcion == '3':
            actualizar_stock(inventario)
        elif opcion == '4':
            mostrar_productos_criticos(inventario)
        elif opcion == '5':
            mostrar_ganancia_potencial(inventario)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def registrar_producto(inventario):
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    valor_compra = float(input("Ingrese el valor de compra del producto: "))
    valor_venta = float(input("Ingrese el valor de venta del producto: "))
    stock_minimo = int(input("Ingrese el stock mínimo permitido: "))
    stock_maximo = int(input("Ingrese el stock máximo permitido: "))
    proveedor = input("Ingrese el nombre del proveedor del producto: ")
    producto = Producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)
    inventario.registrar_producto(producto)
    print("Producto registrado con éxito.")

def actualizar_stock(inventario):
    codigo = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a agregar/restar al stock: "))
    inventario.actualizar_stock(codigo, cantidad)
    print("Stock actualizado con éxito.")

def mostrar_productos_criticos(inventario):
    productos_criticos = inventario.productos_criticos()
    if productos_criticos:
        print("Productos críticos:")
        for producto in productos_criticos:
            print(f"{producto.nombre} (Stock actual: {producto.stock_actual}, Stock mínimo: {producto.stock_minimo})")
    else:
        print("No hay productos críticos.")

def mostrar_ganancia_potencial(inventario):
    ganancia_total = inventario.ganancia_potencial_total()
    print(f"La ganancia potencial total es: {ganancia_total}")

if __name__ == "__main__":
    main()
