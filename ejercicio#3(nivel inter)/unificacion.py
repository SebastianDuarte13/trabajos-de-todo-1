class Producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.proveedor = proveedor
        self.stock_actual = 0

    def actualizar_stock(self, cantidad):
        self.stock_actual += cantidad

    def ganancia_potencial(self):
        return (self.valor_venta - self.valor_compra) * self.stock_actual


class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def visualizar_productos(self):
        for producto in self.productos:
            print(f"Código: {producto.codigo}")
            print(f"Nombre: {producto.nombre}")
            print(f"Valor de compra: {producto.valor_compra}")
            print(f"Valor de venta: {producto.valor_venta}")
            print(f"Stock mínimo: {producto.stock_minimo}")
            print(f"Stock máximo: {producto.stock_maximo}")
            print(f"Proveedor: {producto.proveedor}")
            print(f"Stock actual: {producto.stock_actual}")
            print("--------------------------")

    def actualizar_stock(self, codigo, cantidad):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.actualizar_stock(cantidad)
                break

    def productos_criticos(self):
        productos_criticos = []
        for producto in self.productos:
            if producto.stock_actual < producto.stock_minimo:
                productos_criticos.append(producto)
        return productos_criticos

    def ganancia_potencial_total(self):
        ganancia_total = 0
        for producto in self.productos:
            ganancia_total += producto.ganancia_potencial()
        return ganancia_total


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
        elif opcion == '2':
            inventario.visualizar_productos()
        elif opcion == '3':
            codigo = input("Ingrese el código del producto: ")
            cantidad = int(input("Ingrese la cantidad a agregar/restar al stock: "))
            inventario.actualizar_stock(codigo, cantidad)
            print("Stock actualizado con éxito.")
        elif opcion == '4':
            productos_criticos = inventario.productos_criticos()
            if productos_criticos:
                print("Productos críticos:")
                for producto in productos_criticos:
                    print(f"{producto.nombre} (Stock actual: {producto.stock_actual}, Stock mínimo: {producto.stock_minimo})")
            else:
                print("No hay productos críticos.")
        elif opcion == '5':
            ganancia_total = inventario.ganancia_potencial_total()
            print(f"La ganancia potencial total es: {ganancia_total}")
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
