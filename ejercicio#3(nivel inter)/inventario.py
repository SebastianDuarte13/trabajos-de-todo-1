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
